import sys

sims = [] 
for line in sys.stdin:
    a, b, s = line.split('|')
    s = float(s)
    sims += [(a, b, s)]

query = sys.argv[1]
hits = []
for triplet in sims:
    if query == triplet[0] or query == triplet[1]:
        hits += [triplet]

for a, b, s in sorted(hits, key = lambda x: x[2], reverse = False):
    if query == a:
        print(str(int(s)) + ':' + b)
    else:
        print(str(int(s)) + ':' + a)
