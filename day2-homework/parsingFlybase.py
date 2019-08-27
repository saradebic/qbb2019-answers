#!/usr/bin/env python3

"""program to parse the Uniprot mapping of Flybase genes"""

import sys

print("FlybaseIDS" + "\t" + "Uniprot IDs")


for i, line in enumerate(sys.stdin):
    columns =  line.rstrip("\n").split()
    if "FBgn" not in line:
        continue
    for field in columns:
        if field.endswith("_DROME"):
            print(columns[-1] + "\t" + columns[-2])
            
            

        
            
            