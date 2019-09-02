#!/usr/bin/env python3

"""Usage ./03-boolean.py <ctab> <chr> <fpkm>
subset using boolean filters"""

import sys
import pandas as pd

ctab = pd.read_csv(sys.argv[1], sep="\t")

goi = ctab.loc[:, "FPKM"] > float(sys.argv[3])
goi2 = ctab.loc[:,"chr"] == sys.argv[2] 

print(ctab.loc[goi & goi2,:])
