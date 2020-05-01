import sys

def nearest_neighbor_cluster(triplets):
    index = {}
    for _, a, b in sorted(triplets, reverse=True):
        if not a in index: 
            cluster = index.get(b, set())
            cluster.update([a, b])
            index[a] = cluster
        if not b in index: 
            cluster = index.get(a, set())
            cluster.update([a, b])
            index[b] = cluster
    return set(tuple(cluster) for cluster in index.values())

if __name__ == "__main__":
    lookup = {}
    for line in open(sys.argv[1]).read().splitlines():
        uid, animal = line.split(':')
        lookup[uid] = animal
    triplets = []
    for line in sys.stdin:
        a, b, s = line.split('|')
        a = a.split('/')[3]
        b = b.split('/')[3]
        s = int(s)
        triplets += [(s, lookup[a], lookup[b])]
    clusters = nearest_neighbor_cluster(triplets)
    for cl in clusters:
        print(', '.join(cl))
