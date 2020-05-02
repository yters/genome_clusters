#!/bin/sh
p=$1
a=$(echo $2 | cut -f 1 -d ':')
b=$(echo $2 | cut -f 2 -d ':')
python diff.py $p $a $b
