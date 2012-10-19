#! /usr/bin/env python
#takes the model file and align file and prints out the probability of the dictionary entries used in the align file
import sys
from collections import defaultdict

data = [item.split() for item in map(str.strip,[line for line in open(sys.argv[1])])]
#print data
used = defaultdict(int)

for line in data :
	for graph,phon in zip(line[0].split('|'),line[1].split('|')) :
		used["%s %s"%(graph.replace(':',''),phon.replace(':',''))] +=1

model = [item.split('\t') for item in map(str.strip,[line for line in open(sys.argv[2])])]
probs = {}
for line in model :
	probs["%s %s"%(line[0],line[1])] = line[2]

for item in used :
	if item == ' ' :
		continue
	#print item
	print 'item- ',item,' prob- ',probs[item]	
#print len(used.keys())

