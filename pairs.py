import os
import sys
from itertools import combinations
files = os.listdir(sys.argv[1])
for a, b in combinations(files, 2):
    print(a+':'+b)
