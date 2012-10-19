#! /bin/bash

num_iter=( 1000 2500 5000 7500 10000 )
beta_list=( 1.25 1 0.75 0.5 0.25 1 )
for iter in ${num_iter[@]}
do
for beta in ${beta_list[@]}
do
echo $iter
echo $beta
./m2m-aligner -i cmu.part0.first1000 --delX --nBest 1 --cutoff 10 --maxFn joint --ashish --beta $beta --pgdIter $iter
python getDict.py cmu.part0.first1000.m-mAlign.2-2.delX.1-best.joint.ashish.align
grep '\bBO	' cmu.part0.first1000.m-mAlign.2-2.delX.1-best.joint.ashish.align.model | grep -v 'e-' | sort -nk 3
done
done
