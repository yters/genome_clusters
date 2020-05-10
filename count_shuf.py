import sys
from random import sample

lines = sys.stdin.read().splitlines()

count = 0
for line in lines:
    _, _, c = line.split('|')
    c = float(c)
    if c <= float(sys.argv[1]): 
        count += 1

for line in sample(lines, count):
    print(line)
