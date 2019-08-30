#!/usr/bin/env python3

"""Usage: ./promoterRegions.py <t_data.ctab> """

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

ctab = pd.read_csv(sys.argv[1], sep="\t")
all_start_end_values = ctab.loc[:,["chr", "t_name", "strand", "start", "end"]]

for index, row in all_start_end_values.iterrows():
    if row.loc["strand"] == "+":
        promoterStart = int(row.loc["start"])
        promoter_start_plus_500 = promoterStart + 500
        promoter_start_minus_500 = promoterStart - 500
        if promoter_start_plus_500 <= 0:
            promoter_start_plus_500 = 1
        elif promoter_start_minus_500 <= 0:
            promoter_start_minus_500 = 1
        print(str(row.loc["chr"]) + "\t" + str(promoter_start_minus_500) + "\t" + str(promoter_start_plus_500) + "\t" + str(row.loc["t_name"]))
    elif row.loc["strand"] == "-":    
        promoterStart = int(row.loc["end"])
        promoter_start_plus_500 = promoterStart + 500
        promoter_start_minus_500 = promoterStart - 500
        if promoter_start_plus_500 < 0:
            promoter_start_plus_500 = 1
        elif promoter_start_minus_500 < 0:
            promoter_start_minus_500 = 1
        print(str(row.loc["chr"]) + "\t" + str(promoter_start_minus_500) + "\t" + str( promoter_start_plus_500) + "\t" + str(row.loc["t_name"]))
    
        



