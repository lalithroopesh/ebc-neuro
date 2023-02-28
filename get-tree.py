# Lalith Roopesh 2023

import sqlite3
from ete3 import NCBITaxa, Tree, TreeStyle, NodeStyle, TextFace
# import os, fnmatch, sys

ncbi = NCBITaxa()
file_name = ""

while not(".csv" in file_name):
    file_name = str(input("Enter reading file name (must be .csv): "))

oxlist_raw = []
afflist_raw = []

with open(file_name, "r") as file:
    lines = file.readlines()
    for l in lines:
        oxlist_raw.append(int(l.split(",")[0]))
        afflist_raw.append(float(l.split(",")[1]))

print("Read {} records".format(len(oxlist_raw)))

receptor_name = str(input("Enter receptor name (ex. DRD2): "))

oxlist = []
afflist = []

# clean data to create average affinity per species

for ox in oxlist_raw:
    if not(ox in oxlist):
        indices = [i for i,x in enumerate(oxlist_raw) if x == ox]
        affvals = [afflist_raw[i] for i in indices if not(afflist_raw[i] == 0)]
        oxlist.append(ox)
        if sum(affvals) == 0:
            afflist.append(0)
        else:
            afflist.append(float(sum(affvals)/len(affvals))*-1)

# print(oxlist)
# print(afflist)

# normalize affinities to [0, 1]

m_afflist = list(afflist)
while 0 in m_afflist:
    m_afflist.remove(0)

max_aff = max(m_afflist)
min_aff = min(m_afflist)

for x in range(0,len(afflist)):
    afflist[x] = (afflist[x] - min_aff)/ (max_aff - min_aff)

# print(afflist)

t = ncbi.get_topology(oxlist)
# UNCOMMENT FOR COMMON NAMES GENERATION
# common_names = ncbi.get_common_names(oxlist)
# sci_names = ncbi.get_taxid_translator([str(o) for o in oxlist])
    
# determine node color by affinity

def nlayout(node):
    node.img_style["hz_line_width"] = 1
    node.img_style["vt_line_width"] = 1
    if node.is_leaf():
        ind = oxlist.index(int(node.name))
        aff = afflist[ind]
        # UNCOMMENT FOR COMMON NAME GENERATION
        # if int(node.name) in common_names:
        #    node.name = str(common_names[int(node.name)])
        # elif int(node.name) in sci_names:
        #    node.name = str(sci_names[int(node.name)])
        if aff >= 0:
            b = int(max(0, 255*(1 - 2*aff)))
            r = int(max(0, 255*(2*aff - 1)))
            g = 255 - b - r
            # print("r: {}, g: {}, b: {}".format(r,g,b))
            node.img_style["size"] = 0
            node.img_style["bgcolor"] = "#B3{:02x}{:02x}{:02x}".format(r, g, b)
        else:
            node.img_style["size"] = 3
            node.img_style["fgcolor"] = "black"
            node.img_style["bgcolor"] = "#00000000"
    else:
        node.name = ""
        node.img_style["size"] = 0
        node.img_style["fgcolor"] = "black"

ts = TreeStyle()
ts.show_leaf_name = True
ts.mode = "c"
# ts.arc_start = -180 # 0 degrees = 3 o'clock
ts.arc_span = 360

ts.layout_fn = nlayout
ts.show_branch_support = False
ts.scale = 15
# ts.extra_branch_line_type = 2
ts.extra_branch_line_color = "black"
ts.show_scale = False

# test
text = TextFace(receptor_name)
t.add_face(text, column = 0, position="branch-top")

output_name = ""
while not(".svg" in file_name):
    output_name = str(input("Enter output file name (must be .svg): "))

t.render(output_name, tree_style = ts)

print("Successfully created tree " + output_name)
