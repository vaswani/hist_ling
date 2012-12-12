import sys
def reader(file):
    for line in open(file):
        yield line.split('\t')
def generateTrainingPairs(sent1,sent2):
    #print 'in generate'
    for word1,word2 in ((x,y) for x in sent1.split() for y in sent2.split()) :
        yield '%s\t%s'%(word1,word2)
    
def main():
    f1 = list(reader(sys.argv[1]))
    f2 = list(reader(sys.argv[2]))
    f1_counter = 0
    f2_counter = 0
    while(f1_counter < len(f1) and f2_counter < len(f2)):
        #matching the seg ids
        if f1[f1_counter][0] == f2[f2_counter][0] :
            #print "%s\t%s"%(f1[f1_counter][1].strip(),f2[f2_counter][1].strip())
            new_data = dict((item,1) for item in generateTrainingPairs(f1[f1_counter][1].strip(),f2[f2_counter][1].strip()))
            for item in new_data :
                print item
            f1_counter += 1
            f2_counter += 1
        elif f1[f1_counter][0] > f2[f2_counter][0] :
            f2_counter += 1
        else :
            f1_counter += 1
if __name__=="__main__":
    main()
