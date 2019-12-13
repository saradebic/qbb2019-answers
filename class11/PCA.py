#!/usr/bin/env python3
''' single-cell RNAseq data analysis '''

import scanpy.api as sc
import sys
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)

sc.tl.pca(adata)
sc.pl.pca(adata, ax=ax1, show=False)

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
sc.tl.pca(adata)
sc.pl.pca(adata,ax=ax2, show=False)

sc.pp.neighbors(adata)
sc.tl.louvain(adata)
sc.pl.tsne(adata, ax=ax3)


plt.savefig('PCA.png')
plt.close()


