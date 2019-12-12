#!/usr/bin/env python2
''' Predict gene activity based on interactions with enhancers/TSSs
Usage: activity_by_contact_expression.py <bed_file1_activity> <bed_file2_RNA> '''

import hifive
import numpy
import sys 

hic = hifive.HiC('class13_project', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

activity_dictionary = {}
RNA_dictionary = {}

my_file = sys.argv[1]

for line in open(my_file):
	if line.startswith('track'):
		continue
	fields = line.rstrip('\n').split()
	if int(fields[1]) > 5000000 and int(fields[2]) < 50000000:
		# print(fields[2])
		index = (int(fields[2]) - 5000000) / 5000
		# print(index)
		# print(fields[4])
		if index <= 7000:
			activity_dictionary[index] = float(fields[4])
          
for line in open(sys.argv[2]):
	if line.startswith('track'):
		continue
	fields = line.rstrip('\n').split()
	if int(fields[1]) > 5000000 and int(fields[2]) < 50000000:
		index = (int(fields[2]) - 5000000) / 5000
		if index <= 7000:
			RNA_dictionary[index] = float(fields[4])
 
final_dict = {x:activity_dictionary[x] for x in activity_dictionary 
										if x in RNA_dictionary}

#print(len(final_dict))
# print(len(activity_dictionary))
# print(len(RNA_dictionary))
for i in final_dict:
	# print(data[:,i])
	# print(activity_dictionary[i])
	#print(data[:,i] * activity_dictionary[i])
	data[:,i] *= activity_dictionary[i]

    
data_subset = data[RNA_dictionary.keys(), :][:, activity_dictionary.keys()] 
#print(data_subset.shape)

expression_predictions = numpy.sum(data_subset, axis=1)
#print(len(expression_predictions))
#print(len(expression_predictions))
for count,i in enumerate(final_dict):
	print(str(i) + '\t' + str(expression_predictions[count]))

expression_values = RNA_dictionary.values()
#print(len(expression_values))
R = numpy.corrcoef(expression_values, expression_predictions)[0, 1]
print('R coefficient from linear regression is: '  + str(R)) 
    



