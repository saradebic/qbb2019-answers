#!/usr/bin/env python3 
''' Cluster gene expression data for 6 hematopoetic cell types. Create dendrogram of cell types. Produce heatmap.
Usage: ./heatmap.py <gene_expression_table>'''

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy 
import scipy.cluster.hierarchy as hac
import seaborn as sbrn
from scipy.cluster.vq import whiten,kmeans
from sklearn.cluster import KMeans
from scipy.stats import ttest_rel
    
df = pd.read_csv(sys.argv[1], sep ='\t', header = 0, index_col = 0)
cell_types = list(df.columns)
array = np.array(df)
# print(array)
celltype_array = np.transpose(array)

Z = hac.linkage(df, 'average')
Y = hac.linkage(celltype_array, 'average')
s = hac.leaves_list(Z)
sorted_celltypes = hac.leaves_list(Y)

list_for_sorted_array = []
list_for_sorted_array_celltypes = []
for i in s:
    list_for_sorted_array.append(array[i])
    
for i in sorted_celltypes:
    list_for_sorted_array_celltypes.append(celltype_array[i])
    
 ### create heatmaps    
sorted_array = np.asarray(list_for_sorted_array)
sorted_array_celltypes = np.asarray(list_for_sorted_array_celltypes)
fig, (ax1, ax2) = plt.subplots(ncols=2)
sbrn.heatmap(sorted_array, ax=ax1)
sbrn.heatmap(np.transpose(sorted_array_celltypes),ax=ax2)
ax1.title.set_text('Heatmap based on genes')
ax2.title.set_text('Heatmap based on celltypes')
ax1.set_xlabel('cell types')
ax2.set_xlabel('cell types')
ax1.set_ylabel('Genes')
ax2.set_ylabel('Genes')
plt.tight_layout()
fig.savefig('heatmap_all.png')
plt.close()

### create dendrogram based on cell types
fig,ax = plt.subplots()
labels = [cell_types[1],cell_types[2], cell_types[0], cell_types[4], cell_types[3], cell_types[5]]
hac.dendrogram(Y, labels=labels)
plt.savefig('dendrogram.png')
plt.close()

### k-means - not as good as scikit learn
CFU_and_poly = array[:, [0, 1]]
# print(CFU_and_poly)
# print(CFU_and_poly)
# whitened = whiten(CFU_and_poly)
# codebook, distortion = kmeans(whitened,6)
# print(codebook)

# list_of_clusters_for_each_gene = []
# for i in CFU_and_poly:
#     distances_to_centroids=[]
#     for j in codebook:
#         distance_to_centroid=np.sqrt((j[0]-i[0])**2 + (j[1]-i[1])**2)
#         distances_to_centroids.append(distance_to_centroid)
#         least_distance=min(distances_to_centroids)
#     centroid_index = distances_to_centroids.index(least_distance)
#     list_of_clusters_for_each_gene.append(centroid_index)

# fig, ax = plt.subplots()   
# plt.scatter(CFU_and_poly[:,0],CFU_and_poly[:,1], c=list_of_clusters_for_each_gene, cmap='rainbow')
# plt.savefig('kmeans_normal.png')
# plt.close()

### sklearn k-means
kmeans = KMeans(n_clusters=6, random_state=0, n_init=4).fit_predict(CFU_and_poly)
#print(kmeans)
fig, ax = plt.subplots()
plt.scatter(CFU_and_poly[:,0],CFU_and_poly[:,1], c=kmeans, cmap='rainbow')
ax.title.set_text('K-means clustering of CFU and Poly cell types')
ax.set_xlabel('CFU cell type')
ax.set_ylabel('Poly cell type')
plt.savefig('kmeans.png')
plt.close()


### find differentially expressed genes between two earliest and two latest stages 

two_earliest = array[:, [0,2]] # ???
two_latest = array[:, [1,3]] # ???

p_values = []

for i in range(int(np.size(array,0) - 1)):
	t, p = ttest_rel(two_earliest[i,:], two_latest[i,:])
	p_values.append(p)

indexNamesArr = df.index.values
index_of_DE_genes = []
sig_p_values = []

for index,p_value in enumerate(p_values):
	if p_value <= 0.05:
		index_of_DE_genes.append(index)
		sig_p_values.append(p_value)

#print(indexNamesArr[index_of_DE_genes])


sorted_sig_p_values = sorted(sig_p_values)

for p in sorted_sig_p_values:
	i = p_values.index(p)
	gene = indexNamesArr[i]
	#print(gene)
	if df.loc[gene, 'poly'] > df.loc[gene, 'CFU'] and df.loc[gene, 'poly'] > df.loc[gene, 'unk']: #df.loc[gene, 'poly'] > df.loc[gene, 'CFU'] and df.loc[gene, 'poly'] > df.loc[gene, 'unk'] and df.loc[gene, 'int'] > df.loc[gene, 'CFU'] and df.loc[gene, 'int'] > df.loc[gene, 'unk']:
		most_up_gene = gene
		# print(most_up_gene)
		cluster_Nupr1 = kmeans[i]
		# print(cluster_Nupr1)
		break 

### Adcy6 upregulated between int and CFU/unk, Nupr1 upregulated between poly and CFU/unk

fig, ax = plt.subplots()
plt.scatter(CFU_and_poly[:,0],CFU_and_poly[:,1], c=kmeans, cmap='rainbow')
plt.scatter(df.loc['Nupr1', 'CFU'], df.loc['Nupr1', 'poly'], c='black')
ax.title.set_text('K-means clustering of CFU and Poly cell types')
ax.set_xlabel('CFU cell type')
ax.set_ylabel('Poly cell type')
plt.savefig('kmeans.png')
plt.close()

kmeans_list = np.ndarray.tolist(kmeans)
genes_in_same_cluster = []

for count, k in enumerate(kmeans_list):
	if k == 2:
		genes_in_same_cluster.append(count)

genes = list(df.index.values)

print("The most upregulated gene in the late differentiation stage is Nupr1. Adcy6 is also upregulated but not as significantly. ")
print("Genes in the same kmeans cluster as Nupr1 are: ")

for index in genes_in_same_cluster:
	print(genes[index])

print("Genes that are differentially expressed between the two earliest and two latest stages are:")

for i in index_of_DE_genes:
	print(genes[i])

print("The role of Nupr1 is reported to be negative regulation of the cell cycle, and as such it inhibits the proliferation of differentiated cells. Cells, in general, as they differentiate lose their proliferative potential. Therefore, Nupr1 being upregulated in late differentiation stages of cells makes sense.")





