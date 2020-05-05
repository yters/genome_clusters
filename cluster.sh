#!/bin/sh
#ls genomes/ | xargs -I {} ./process_genome.sh {} > log.txt
#python pairs.py sdbfs | xargs -I {} ./all_pairs_dist.sh sdbfs {} > distances.txt
#python3 match_id_animal.py genomes/ > lookup.txt
cat distances.txt | python cluster.py lookup.txt 0 1 True > clusters.txt
