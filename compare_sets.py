import os
import scipy.stats as sp
import statistics as s

def create_array(path):
    affin_arr = []
    files = os.listdir(path)
    for file in files:
        with open(path+"/"+file, "r") as f:
            lines = f.readlines()
            # print(lines[1].split(" "))
            affin = float(lines[1].split(" ")[8])
            affin_arr.append(affin)
    return affin_arr

expected_arr = create_array("./small_neurodocking_results")
observed_arr = create_array("./big_neurodocking_results")

contingency_table = [[observed_arr[i], expected_arr[i]] for i in range(len(observed_arr))]
chi2_table = [[observed_arr[i]*-1, expected_arr[i]*-1] for i in range(len(observed_arr))]
print(contingency_table)


diffs = []
for r in contingency_table:
    diffs.append(r[0]-r[1])
# print("average diff: {}\nmax diff: {}".format(s.mean(diffs), max(diffs)))

print(diffs)

t_stat, p = sp.ttest_1samp(a=diffs,popmean=0)
print("null hypothesis is that they are the same. t stat: {} and p-value: {}".format(t_stat,p))

# manual t-test
x = s.mean(diffs)
s_x = s.stdev(diffs)
u_x = 0
se_x = s_x/pow(len(diffs),0.5)
t_df = (x-u_x)/se_x
df = len(diffs)-1
print("x = {}, s_x = {}, n = {}".format(x, s_x, len(diffs)))
print("t_df = {} with df = {}".format(t_df, df))