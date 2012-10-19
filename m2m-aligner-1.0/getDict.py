#! /usr/bin/env python
import sys
from collections import defaultdict

data = [item.split() for item in map(str.strip,[line for line in open(sys.argv[1])])]
#print data
used = defaultdict(int)

for line in data :
	for graph,phon in zip(line[0].split('|'),line[1].split('|')) :
		used["%s %s"%(graph,phon)] +=1


print len(used.keys())

