#!/usr/bin/env python3

"""Your script should take as input the mapping file (as above) and a c_tab file from StringTie and find 
the corresponding translation from the mapping file. If found, it should print the line from the c_tab file 
with the identifier. If not found, it should do one of two things depending on a command line argument:
Print nothing (ignore the line)
Print and fill the field with a default value

To run, ./identifierMapping.py <mapping file> <c_tab file> <nothing | default>"""

import sys 

# sys.stdin --> file
# sys.argv --> list of strings
# sys.argv[1] --> string
# open(sys.argv[1]) --> file

mapping_file_dictionary = {}
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    columns = line.rstrip("\n").split("\t")
    fbgn = columns[0]
    up = columns[1]
    mapping_file_dictionary[fbgn] = up

for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    columns_ctabfile = line.rstrip("\n").split("\t")
    gene_id = columns_ctabfile[8]
    if gene_id in mapping_file_dictionary:
        print(line.strip() + "The uniprot identifier is: " + mapping_file_dictionary[gene_id])
    elif gene_id not in mapping_file_dictionary and sys.argv[3] == "default":
        print(line.strip() + "The uniprot identifier is: X")
    elif gene_id not in mapping_file_dictionary and sys.argv[3] == "nothing":
        continue
    
   
    
    

        
  
        