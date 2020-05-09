from random import sample
import sys

lines = sys.stdin.read().splitlines()
print('\n'.join([line for line in sample(lines, len(lines))]))
