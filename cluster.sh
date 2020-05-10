#!/bin/sh
ls genomes/ | xargs -I {} ./process_genome.sh {} > log.txt
python pairs.py sdbfs | xargs -I {} ./all_pairs_dist.sh sdbfs {} > distances.txt
cat distances.txt | sort -n -k 3 -t '|' | python cluster.py 0 1 > clusters.txt
