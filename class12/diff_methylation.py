#!/usr/bin/env python3
''' Find differentially methylated cytosines in Mus Musculus chromosome 19.
Usage: ./diff_methylation.py <ES_bedgraph> <EpiSC_bedgraph> / <CpG_OB_SRR1035454_1_bismark_bt2_pe.txt> <CpG_context_SRR1035452_1_bismark_bt2_pe.txt>'''

import sys

ES_methylation_states = {}
EpiSC_methylation_states = {}
diff_methylated_position_ES = []
methylation_diff_sites_status = []

# for line in open(sys.argv[1]):
#     if line.startswith('track'):
#         continue
#     fields = line.split()
#     if float(fields[3]) >= 50:
#         ES_methylation_states[fields[1]] = 1
#     else:
#         ES_methylation_states[fields[1]] = 0

# for line in open(sys.argv[2]):
#     if line.startswith('track'):
#         continue
#     fields = line.split()
#     if float(fields[3]) >= 50:
#         EpiSC_methylation_states[fields[1]] = 1
#     else:
#         EpiSC_methylation_states[fields[1]] = 0   
        
# final_dict = {x:ES_methylation_states[x] for x in ES_methylation_states  
#                               if x in EpiSC_methylation_states} 

# #print(final_dict)
# print('Differentially methylated site' + '\t' + 'Methylation status in ES cells')
 

# for dic in final_dict:
#     if ES_methylation_states[dic] != EpiSC_methylation_states[dic]:
#         diff_methylated_position_ES.append(dic)
#         methylation_diff_sites_status.append(ES_methylation_states[dic])
#         if ES_methylation_states[dic] == 1:
#             print(dic + '\t' + 'methylated')
#         else:
#             print(dic + '\t' + 'unmethylated')
    # if ES_methylation_states[dic] == EpiSC_methylation_states[dic]:
   #      not_DM.append(dic)

# print(diff_methylated_position_ES)
# print(len(diff_methylated_position_ES))
# print(not_DM)

    
   
# print(len(index_of_diff_meth))
# print(len(ES_methylation_states))
# print(len(EpiSC_methylation_states))
  
# print('Differentially methylated sites are in these positions and their methylation state in ES cells is:')
# for count, line in enumerate(open(sys.argv[1])):
#     if line.startswith('track'):
#         continue
#     fields = line.split()
#     if count in index_of_diff_meth:
#         print(fields[1])
#     if count in index_of_diff_meth and float(fields[3]) >= 50:
#         print('methylated')
#     if count in index_of_diff_meth and float(fields[3]) <= 50:
#         print('unmethylated')
        
## Same analysis but using bismark methylation extractor output files 

for line in open(sys.argv[1]):
    if line.startswith('Bismark'):
        continue
    fields = line.split()
    if fields[4] == 'Z':
        ES_methylation_states[fields[3]] = 1
    else:
        ES_methylation_states[fields[3]] = 0

for line in open(sys.argv[2]):
    if line.startswith('Bismark'):
        continue
    fields = line.split()
    if fields[4] == 'z':
        EpiSC_methylation_states[fields[3]] = 1
    else:
        EpiSC_methylation_states[fields[3]] = 0   
        
final_dict = {x:ES_methylation_states[x] for x in ES_methylation_states  
                              if x in EpiSC_methylation_states} 
# print(len(final_dict))
# print(len(ES_methylation_states))
# print(len(EpiSC_methylation_states))

#print(final_dict)
print('Differentially methylated site' + '\t' + 'Methylation status in ES cells')
 

for dic in final_dict:
    if ES_methylation_states[dic] != EpiSC_methylation_states[dic]:
        diff_methylated_position_ES.append(dic)
        methylation_diff_sites_status.append(ES_methylation_states[dic])
        if ES_methylation_states[dic] == 1:
            print(dic + '\t' + 'methylated')
        else:
            print(dic + '\t' + 'unmethylated')
print(len(diff_methylated_position_ES))        
#print(diff_methylated_position_ES)
#print(len(diff_methylated_position_ES))   
    
    