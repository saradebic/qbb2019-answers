#!/usr/bin/env python3

"""Usage: ./hwMetadata.py <metadata.csv> <ctab_dir> e.g. ~/qbb2019-answers/results/stringtie

Create all.csv with FPKMS

t_name, gene_name, sample1, ..., sample_en"""

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

fpkms = {}
for i, line in enumerate(open(metadata)):
    if i==0:
        continue
    fields = line.rstrip("\n").split(",")
    srr_id = fields[0]
    sex_and_num = str(fields[1]) + "_" + str(fields[2])
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    if i==1:
        fpkms["gene_name"] = df.loc[:, "gene_name"]
    fpkms[sex_and_num] = df.loc[:,"FPKM"]

df_fpkms = pd.DataFrame(fpkms)
#print(df_fpkms)
pd.DataFrame.to_csv(df_fpkms, "all.csv")
    