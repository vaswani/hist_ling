#! /bin/bash

grep '<seg id=\"' $1 | perl -ple 's{<seg id=\"(.*?)\" type=\"verse\">(.+?)}{$1\t$2}g' | grep -v '<seg id' | sort -k 1,1
