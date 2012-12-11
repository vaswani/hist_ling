import sys
from optparse import OptionParser
from collections import defaultdict
parser = OptionParser()
parser.add_option("--model_file", action="store", type="string", dest="model_file",default=100,help="the model file")
parser.add_option("--align_file", action="store", type="string", dest="align_file",default=100,help="the alignment file ")
(options, args) = parser.parse_args()
model_file = options.model_file
align_file = options.align_file
model = defaultdict(lambda:defaultdict(int))
for line in open(model_file):
    line = line.strip()
    if line == '':
        continue
    model[line.split()[0]][line.split()[1]] = line.split()[2]
for line in open(align_file):
    line = line.strip()
    if line == '':
        continue

    print "PAIR: \n%s\t%s"%(''.join(line.split('\t')[0].split('|')[:-1]),''.join(line.split('\t')[1].split('|')[:-1]))
    print "ALIGNMENT:"
    for source_seg,target_seg in zip(line.split('\t')[0].split('|')[:-1],line.split('\t')[1].split('|')[:-1] ) :
        print "%s\t%s\t%s\n"%(source_seg,target_seg,str(model[''.join(source_seg.split(':'))][''.join(target_seg.split(':'))]))
