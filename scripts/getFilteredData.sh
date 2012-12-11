#! /bin/bash

awk '$7<0.5 { print $0 }' < $1.lex | grep -v '.*[A-Z].*' | sort -nrk 7 > $1.lex.filtered

awk '{print $1"\t"$2}' < $1.lex.filtered > $1.lex.filtered.pairs

cat $1.lex.filtered.pairs | perl -ple 's{[-\!\;\(\):,.\?]}{}g' | perl -ple 's{\[.*?\]}{}g' | sort | uniq  > $1.lex.filtered.pairs.temp


python makeTrainingData.py $1.lex.filtered.pairs.temp > $1.lex.filtered.pairs.training

perl -i -ple 's{---dir-name---}{'$1'}g' run_1000_10_0.5.pbs
