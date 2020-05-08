To generate clusters from rank based distance
```
cat distances_ranks.txt | sort -n -k 3 -t '|' | python cluster.py 1000000 1
```
from LZJS based similarity
```
cat distances.txt | python neg.py | sort -n -k 3 -t '|' | python cluster.py -1900 1
```

The `cluster.py` script reads distance triplets on stdin and the first arg sets the triplet upper rejection threshold and the second arg is the number of nearest neighbors to form a cluster.

To score a cluster
```
cat clusters.txt | python score_cluster.py kind.txt
```

The `score_cluster.py` script scores a cluster read from stdin using a reference cluster specified as the first arg.
