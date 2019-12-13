#!/usr/bin/env python3
''' single-cell RNAseq data analysis '''

import scanpy.api as sc
import sys
import matplotlib.pyplot as plt

adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.pp.neighbors(adata)
sc.tl.louvain(adata)


sc.tl.rank_genes_groups(adata, groupby ='louvain', method='t-test')
sc.pl.rank_genes_groups(adata, groupby='louvain', method = 't-test', show=False, save='ttest.png')

sc.tl.rank_genes_groups(adata, groupby ='louvain', method='logreg')
sc.pl.rank_genes_groups(adata, groupby='louvain', method = 'logreg', show=False, save='logreg.png')