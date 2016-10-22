# import sys
# file=sys.argv[1]
# file2=sys.argv[2]
# f=open(file, 'r')
# f2 = open(file2, 'w')

# for line in f:
#     line = line.strip('\n ').split()
#     f2.write('%s\n'%' '.join(line))
# f.close()
# f2.close()


import sys
file=sys.argv[1]
file2=sys.argv[2]
file3=sys.argv[3]
f=open(file, 'r')
f2 = open(file2, 'r')
f3 = open(file3, 'w')

for line in f:
    line = line.strip('\n ').split()
    if not line:
        f3.write('\n')
        continue
    word = ' '.join(line[:-1])
    data = f2.readline().strip('\n ')
    f3.write('%s %s\n'%(data, word))
f.close()
f2.close()
