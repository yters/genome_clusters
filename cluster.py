import sys
from itertools import combinations

def nearest_neighbor_cluster(triplets):
    index = {}
    neighbs = {}
    for s, a, b in sorted(triplets, reverse=(sys.argv[4] == 'True')):
        if s > float(sys.argv[2]) and not sys.argv[4] == 'True': break 
        if s < float(sys.argv[2]) and sys.argv[4] == 'True': break 
        if neighbs.get(a, 0) < int(sys.argv[3]): 
            neighbs[a] = neighbs.get(a, 0) + 1
            cluster = index.get(a, set())
            cluster.update([a, b])
            cluster.update(index.get(b, set()))
            index[a] = cluster
            for i in index.get(b, set()):
                index[i] = cluster
        if neighbs.get(b, 0) < int(sys.argv[3]): 
            neighbs[b] = neighbs.get(b, 0) + 1
            cluster = index.get(b, set())
            cluster.update([a, b])
            cluster.update(index.get(a, set()))
            index[b] = cluster
            for i in index.get(a, set()):
                index[i] = cluster
    return set(tuple(cluster) for cluster in index.values())

if __name__ == "__main__":
    lookup = {}
    for line in open(sys.argv[1]).read().splitlines():
        uid, animal = line.split(':')
        lookup[uid] = animal
    triplets = []
    for line in sys.stdin:
        if not '|' in line: continue
        a, b, s = line.split('|')
        a = a.split('.')[0]
        b = b.split('.')[0]
        s = float(s)
        #triplets += [(s, lookup[a], lookup[b])]
        triplets += [(s, a, b)]
    clusters = nearest_neighbor_cluster(triplets)
    for cl in clusters:
        print(', '.join(cl))
