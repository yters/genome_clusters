import sys
from math import log

def parse_cluster(lines, whitelist):
    clusters = {}
    for line in lines:
        cluster = tuple(set([item.strip() for item in line.strip().split(',')]))
        for item in cluster:
            if item in whitelist:
                clusters[item] = cluster
    return clusters

def ent(p):
    if p == 0 or p == 1: return 0
    return -p*log(p,2)

lines = None
whitelist = None

ref_clusters = None
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

ref_items = [item.strip() for line in lines for item in line.split(',')]
whitelist = set(ref_items)
ref_clusters = parse_cluster(lines, whitelist)

lines = sys.stdin.read().splitlines()
gen_items = [item.strip() for line in lines for item in line.split(',')]
gen_clusters = parse_cluster(lines, whitelist)

H_X = 0
total = len(ref_clusters)
for cl in set(ref_clusters.values()):
    p = len(cl)/float(total)
    e = ent(p)
    H_X += e

H_Y = 0
H_XlY = 0
for gen_cl in set(gen_clusters.values()):
    p = len(gen_cl)/float(total)
    H_Y += ent(p)

    cnd_clusters = {}
    for item in gen_cl:
        ref_cl = ref_clusters[item]
        cnd_clusters[ref_cl] = cnd_clusters.get(ref_cl, set()) | set([item])
    cH = 0
    for cnd_cl in cnd_clusters.values():
        p = len(cnd_cl)/float(len(gen_cl))
        e = ent(p)
        cH += e
    cH *= len(gen_cl)/float(total)
    H_XlY += cH

ref_cnt = sum([len(cl) for cl in ref_clusters])
gen_cnt = sum([len(cl) for cl in gen_clusters])

NMI = 0
if H_X+H_Y > 0:
    p = len(gen_items)/float(len(ref_items))
    NMI = p*2*(H_X-H_XlY)/(H_X+H_Y)
print(NMI)
