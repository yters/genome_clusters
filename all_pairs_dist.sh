#!/bin/sh
p=$1
a=$(echo $2 | cut -f 1 -d ':')
b=$(echo $2 | cut -f 2 -d ':')
java -cp jlzjd.jar com.edwardraff.jlzjd.Main -c $p/$a $p/$b | python get_avg.py $a $b
