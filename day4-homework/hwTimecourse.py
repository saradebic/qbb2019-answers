#!/usr/bin/env python3

"""Usage: ./hwTimecourse.py <transcriptname> <replicates.csv> <fpkm file (all.csv)> <ctab-directory> 

Create a timecourse of a given transcript for males and females """

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

ctab_dir = sys.argv[4]
t_name = sys.argv[1]

fpkms = pd.read_csv( open(sys.argv[3]), index_col="t_name" )

# fpkms_replicates = {}
fpkms_replicates = []
for i, line in enumerate(open(sys.argv[2])):
    if i==0:
        continue
    fields = line.rstrip("\n").split(",")
    srr_id = fields[0]
    sex_and_num = str(fields[1]) + "_" + str(fields[2])
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    fpkms_replicates.append(df.loc["FBtr0331261","FPKM"])
    
# print(fpkms_replicates)


#Extract data
def timecourse(sex):
    columns = fpkms.columns                              
    labels = list(columns)[1:9]
    my_sex_samples = []
    my_data = []
    for i in columns:
        if i.startswith(sex):
            my_sex_samples.append(True)
        else:
            my_sex_samples.append(False)

    my_data = list(fpkms.loc[t_name,my_sex_samples])
    return my_data, labels
   
female_data_points, labels =  timecourse("female")
male_data_points, labels = timecourse("male")

developmental_stage = []
for label in labels:
    filler, important = label.split("_")
    developmental_stage.append(important)
    
fig, ax = plt.subplots()
ax.plot(male_data_points, color="blue", label="male")
ax.plot(female_data_points, color="red", label="female")
ax.plot([5,6,7,8],fpkms_replicates[:4],'x', color = "green", label = "male replicates")
ax.plot([5,6,7,8],fpkms_replicates[4:],'x', color="purple", label= "female replicates")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_title(sys.argv[1])
plt.xlabel("Developmental stage")
plt.ylabel("mRNA abundance (RFPKM)")
plt.xticks(np.arange(len(labels)), developmental_stage, rotation="vertical")
plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)
