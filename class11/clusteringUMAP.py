#!/usr/bin/env python3
''' single-cell RNAseq data analysis '''

import scanpy.api as sc
import sys
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

fig, ax = plt.subplots()
sc.pp.neighbors(adata)
sc.tl.louvain(adata)
sc.tl.umap(adata)
sc.pl.umap(adata, color='louvain', ax=ax, legend_loc='on data', show=False)
plt.savefig('umap.png')
plt.close()