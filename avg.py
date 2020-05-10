import sys

avg = []
for line in sys.stdin:
    avg += [int(line)]
print(sum(avg)/float(len(avg)))
