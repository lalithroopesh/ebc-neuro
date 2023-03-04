# Lalith Roopesh 2023

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

drd1_raw = []

drd2_raw = []

oxtr1_raw = []

avpr1_raw = []

x_title = "Receptor"
y_title = "Binding affinity (kJ/mol)"

def clean(data):
    cld = list(data)
    while 0 in cld:
        cld.remove(0)
    return cld
 
drd1 = clean(drd1_raw)
drd2 = clean(drd2_raw)
oxtr1 = clean(oxtr1_raw)
avpr1 = clean(avpr1_raw)

# Dataset:
a = pd.DataFrame({ x_title : np.repeat('DRD1',len(drd1)), y_title: drd1 })
b = pd.DataFrame({ x_title : np.repeat('DRD2',len(drd2)), y_title: drd2 })
c = pd.DataFrame({ x_title : np.repeat('OXTR1',len(oxtr1)), y_title: oxtr1 })
d = pd.DataFrame({ x_title : np.repeat('AVPR1',len(avpr1_raw)), y_title: avpr1_raw })

df=a.append(b).append(c).append(d)

# boxplot

PROPS = {
    'boxprops':{'facecolor':'none', 'edgecolor':'black'},
    'medianprops':{'color':'black'},
    'whiskerprops':{'color':'black'},
    'capprops':{'color':'black'}
}

ax = sns.boxplot(x=x_title, y=y_title, data=df, linewidth = 0.7, showfliers = False, **PROPS)

# add stripplot
ax = sns.stripplot(x=x_title, y=y_title, data=df, color="red", jitter=0.3, size=2)

# add title
plt.title("Distribution of binding affinities (failed runs removed)", loc="center")

# show the graph
plt.show()
