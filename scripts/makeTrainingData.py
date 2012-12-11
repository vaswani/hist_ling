import sys

for line in open(sys.argv[1]):
  line = line.strip()
  if len(line.split()) < 2:
      continue
  print "*%s$\t* %s $"%(line.split()[0],' '.join(line.split()[1]))
