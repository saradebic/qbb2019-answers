#!/usr/bin/env python3
# Creates script which plots the read depth distribution across each called variant
# the genotype quality distribution
# the allele frequency spectrum of your identified variants
# a summary of the predicted effect of each variant as determined by snpEff (barplot?)

# usage: ./VariantAnalysisPlots.py <snpEff_result_file>

import sys
import matplotlib.pyplot as plt
import numpy as np

read_depths = []
genotype_quality = []
allele_frequency = []
#snp_effect = {'upstream_gene_variant': 0, 'downstream_gene_variant': 0, 'non_coding_transcript_exon_variant': 0, 'intron_variant': 0, 'intergenic_region': 0, 'gene_variant': 0, 'exon_variant': 0, 'synonymous_variant': 0, 'stop_retained_variant': 0, 'splice_region_variant': 0, 'missense_variant': 0, 'disruptive_inframe_insertion': 0, 'disruptive_inframe_deletion': 0, 'conservative_inframe_insertion': 0, 'conservative_inframe_deletion': 0, 'stop_lost': 0, 'stop_gained': 0, 'start_lost': 0, 'splice_donor_variant': 0, 'splice_acceptor_variant': 0, 'frameshift_variant': 0 }

snp_effect = {} #alternate way to do it

 
for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    read_depth_slice = line.rstrip("\n").split(";")[7]
    read_depth_value = read_depth_slice.split('=')[1]
    if ',' in read_depth_value:
        read_depth_value = read_depth_value.split(',')[1]
    read_depths.append(float(read_depth_value))

    allele_frequency_slice = line.rstrip("\n").split(";")[3]
    allele_frequency_value = allele_frequency_slice.split('=')[1]
    if ',' in allele_frequency_value:
        allele_frequency_value = allele_frequency_value.split(',')[1]
    allele_frequency.append(float(allele_frequency_value))
                
    fields = line.rstrip("\n").split()
    genotype_quality.append(float(fields[5])) 
        
        
    fields = line.rstrip("\n").split("|")
    # for key in snp_effect:
#         if key in fields[1]:
#             snp_effect[key] += 1
    if fields[1] not in snp_effect:   #alternate way to do it
        snp_effect[fields[1]] = 1
    elif fields[1] in snp_effect:
        snp_effect[fields[1]] += 1

# print(read_depths)
# print(allele_frequency)
# print(genotype_quality)

fig, ax = plt.subplots(2,2)
ax[0,0].hist(read_depths, range = [0,750], bins = 100)
ax[0,0].set_xlabel('Read depths')
# ax[0,0].xaxis.set_major_locator(plt.MaxNLocator(5))
ax[0,0].yaxis.set_major_locator(plt.MaxNLocator(5))
ax[0,1].hist(genotype_quality, range = [0,2000], bins = 100)
ax[0,1].set_xlabel('Genotype quality')
# ax[0,1].xaxis.set_major_locator(plt.MaxNLocator(9))
ax[0,1].yaxis.set_major_locator(plt.MaxNLocator(5))
ax[1,0].hist(allele_frequency, bins = 100)
ax[1,0].set_xlabel('Allele frequency')
# ax[1,0].xaxis.set_major_locator(plt.MaxNLocator(4))
ax[1,0].yaxis.set_major_locator(plt.MaxNLocator(5))
ax[1,1].bar(snp_effect.keys(), snp_effect.values())
ax[1,1].set_xlabel('Snp effect')
ax[1,1].set_xticklabels(snp_effect.keys(), rotation='vertical', fontsize=4.2)
ax[1,1].yaxis.set_major_locator(plt.MaxNLocator(5))
for x in ax.flat:
    x.set(ylabel='Frequency')
plt.tight_layout()
fig.savefig("VariantAnalysis.png")
plt.close(fig)

            
    
    

        
