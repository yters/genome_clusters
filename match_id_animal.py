import os
import sys

path = sys.argv[1]
for file in os.listdir(path):
    print(open(os.path.join(path, file)).read().strip() + ':' + file)
