import sys

def next():
    for line in sys.stdin:
        yield line.strip().split()

def main():
    for item in next():
        print item
        #print verse

if __name__=="__main__":
    main()
main()
