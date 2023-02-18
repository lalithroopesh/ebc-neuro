# Lalith Roopesh 2023

import os, fnmatch, sys

x = ""
while not(x.lower() == "y"):
    x = str(input("Confirm all of your _output.pdbqt files are in the in the {} folder (same as this script). (y/n) > ".format(os.getcwd())))

rec_name = str(input("Enter your template name. Don't use special characters (besides _ and -) ex. 70ft-1 > "))
job_name = rec_name + "_results"

files = os.listdir("./")

output_files = []
for f in files:
    if fnmatch.fnmatch(f, "*_output.pdbqt"):
        output_files.append(f)

results = []
for o in output_files:
    new_r = [o.split("_")[0],o.split("_")[1],rec_name]
    with open(o, "r") as sel_out:
        lines = sel_out.readlines()
        for l in lines:
            if (l[:19] == "REMARK VINA RESULT:"):
                new_r.append([i for i in l.split(" ") if i != " "][8])
    results.append(new_r)

r_final = []
for item in results:
    r_final.append(",".join(item)+"\n")

with open("{}.csv".format(job_name),"w") as compiled_results:
    compiled_results.writelines(r_final)
    print("Wrote file {}.csv".format(job_name))
