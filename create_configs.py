# Lalith Roopesh 2022

import os, fnmatch, sys

# confirmations
x = ""
while not(x.lower() == "y"):
    x = str(input("Confirm that ONLY the PDBQTs with the same grid box are in the folder this file is in. (y/n) > "))
x = ""
while not(x.lower() == "y"):
    x = str(input("Confirm that your ligand (ex. dopamine, vasopressin, or oxytocin) are in the folder as a PDBQT file (y/n) > "))

# some job parameters

r_possible = ["oxytocin", "dopamine", "vasopressin"]


rname = ""
while not(rname in r_possible):
    rname = str(input("""Enter your ligand file name. Your file should be named this name with .pdbqt ONLY.
Possibilities are: oxytocin, dopamine, vasopressin
> """))

job_name = str(input("Enter the name of the job. Don't use special characters (besides _ and -) ex. OXTR1_1-39. > "))
netid = str(input("Enter your NetID > "))

# config variables

center_x = float(input("Input center_x: "))
center_y = float(input("Input center_y: "))
center_z = float(input("Input center_z: "))
size_x = float(input("Input size_x: "))
size_y = float(input("Input size_y: "))
size_z = float(input("Input size_z: "))

# standardized config variables

exhaustiveness = 64
cpu = 24

decision = str(input("""
=======================================================================

Here are your docking settings:

JOB DETAILS
> Job name: {}
> Ligand: {}
> Your NetID: {}
> Working directory: {}

CONFIG SETTINGS
> center_x = {}
> center_y = {}
> center_z = {}
> size_x = {}
> size_y = {}
> size_z = {}

STANDARDIZED SETTINGS
> The research organizers have standardized the following values:
> exhaustiveness = {}
> cpu = {}

REVIEW
> This command will overwrite all files currently in this directory.
> Review the previous information.
> Proceed? (y/n)
> """.format(job_name, rname, netid, os.getcwd(), center_x, center_y, center_z, size_x, size_y, size_z, exhaustiveness, cpu)))

if not(decision.lower() == "y"):
    sys.exit("Job approval authorization 'y' denied. Job terminated.")

# get files

files = os.listdir("./")

pdbqt_files = []
for f in files:
    if fnmatch.fnmatch(f, "*.pdbqt") and not(f == rname):
        pdbqt_files.append(f)

pdbqt_files.remove("{}.pdbqt".format(rname))

config_files = []
for p in pdbqt_files:
    pdata = p.split("_")
    cname = "{}_{}_config.txt".format(pdata[0], pdata[1])
    with open(cname, "w") as config:
        config.write("receptor = {}\nligand = {}.pdbqt\ncenter_x = {}\ncenter_y = {}\ncenter_z = {}\nsize_x = {}\nsize_y = {}\nsize_z = {}\nexhaustiveness = {}\ncpu = {}\nout = {}_{}_output.pdbqt".format(p, rname, center_x, center_y, center_z, size_x, size_y, size_z, exhaustiveness, cpu, pdata[0], pdata[1]))
        print("Created file {}".format(cname))
        config_files.append(cname+"\n")

with open("{}_list.txt".format(job_name),"w") as configlist:
    configlist.writelines(config_files)
    print("Created file {}_list.txt".format(job_name))

with open("{}.sh".format(job_name),"w") as job:
    job.write("""#!/bin/bash\n#SBATCH --job-name={}\n#SBATCH --time=15:00:00\n#SBATCH --mail-type=END\n#SBATCH --mail-user={}@usf.edu\n#SBATCH --mem=60480\nreadarray -t files < {}_list.txt\nfor file in "${{files[@]}}"; do\n./vina --config "$file"\ndone""".format(job_name, netid, job_name))
    print("Created file {}.sh".format(job_name))
    