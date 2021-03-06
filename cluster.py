import sys
from itertools import combinations

threshold = float('inf')
num_neighbs = 1
def nearest_neighbor_cluster(triplets):
    index = {}
    for s, a, b in triplets:
        index[a] = set([a])
        index[b] = set([b])
    neighbs = {}
    for s, a, b in triplets:
        if s > threshold: continue
        if neighbs.get(a, 0) < num_neighbs: 
            neighbs[a] = neighbs.get(a, 0) + 1
            cluster = index.get(a, set())
            cluster.update([a, b])
            cluster.update(index.get(b, set()))
            index[a] = cluster
            for i in index.get(b, set()):
                index[i] = cluster
        if neighbs.get(b, 0) < num_neighbs: 
            neighbs[b] = neighbs.get(b, 0) + 1
            cluster = index.get(b, set())
            cluster.update([a, b])
            cluster.update(index.get(a, set()))
            index[b] = cluster
            for i in index.get(a, set()):
                index[i] = cluster
    return set(tuple(cluster) for cluster in index.values())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_neighbs = int(sys.argv[1])
    if len(sys.argv) > 2:
        threshold = float(sys.argv[2])
    triplets = []
    for line in sys.stdin:
        if not '|' in line: continue
        a, b, s = line.split('|')
        a = a.split('.')[0]
        b = b.split('.')[0]
        s = float(s)
        triplets += [(s, a, b)]
    clusters = nearest_neighbor_cluster(triplets)
    for cl in clusters:
        print(', '.join(cl))
