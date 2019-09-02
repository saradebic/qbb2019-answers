#!/usr/bin/env python3

"""Usage: ./thresholdFpkm.py <threshold> <criteria> <ctab1> <ctab2> .... <ctab_n> >

Only reporting transcripts that exceed a threshold FPKM. Criteria is if rowsum exceeds threshold (type "row")
or one sample exceeds threshold (type "sample")"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpkm = {}
for i in range (3, len(sys.argv)):
    ctab = open(sys.argv[i])
    ctab = pd.read_csv(sys.argv[i], sep="\t", index_col="t_name")
    fpkm[sys.argv[i].split(os.sep)[-2]] = ctab.loc[:,"FPKM"]
    

# print(fpkm)
df = pd.DataFrame(fpkm)
# print(df)
if sys.argv[2] == "row":
        rows = df.sum(axis=1) > float(sys.argv[1])
        newDf = df.loc[rows,:]
        
elif sys.argv[2] == "sample":
        samples = df.max(axis=1) > float(sys.argv[1])
        newDf = df.loc[samples,:]

    
print(newDf)    
        
        