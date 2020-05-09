#!/bin/sh
set -e
echo processing $1
date
cd genomes
datasets download assembly --inputfile $1 --filename $1.zip
rm -rf tmp
mkdir tmp
mv $1.zip tmp/
cd tmp
unzip $1.zip
rm $1.zip
for fna in `find ./ -name "*.fna"`; do sed '/[^gatcGATC]/d' $fna >> all.fna; rm $fna; done
split -b 10M all.fna $fna.piece.
for piece in `find ./ -name "*.piece.*"`; do java -cp ~/jlzjd.jar com.edwardraff.jlzjd.Main $piece -o $piece.sdbf; rm $piece; done
touch ~/sdbfs/$1.sdbf
find ./ -name "*.sdbf" | xargs -I {} cat {} >> ~/sdbfs/$1.sdbf
rm -rf tmp
