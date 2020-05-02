import os
import sys

p = sys.argv[1]
f1 = sys.argv[2]
f2 = sys.argv[3]
r1 = {w:i for i, w in enumerate(open(os.path.join(p, f1)).read().splitlines())}
r2 = {w:i for i, w in enumerate(open(os.path.join(p, f2)).read().splitlines())}
diff = 0
for w in r1.keys():
    if not w in r1 or not w in r2: continue
    diff += abs(r1[w]-r2[w])
print(sys.argv[2]+'|'+sys.argv[3]+'|'+str(diff))
