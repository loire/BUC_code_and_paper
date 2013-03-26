#!/bin/bash

# usage ./ENCprime_laucher.sh ORF_file code 

# Dependence: seqfilebreak.pl ; SeqCount ENCprime
# https://www.eeb.ucla.edu/Faculty/Novembre/software/software.html
# http://ib.berkeley.edu/labs/slatkin/munch/scriptlist/seqfilebreak.txt
# http://emboss.open-bio.org/rel/dev/apps/seqcount.html
# Input: ORF file

# $1 ORF fasta file
seqfilebreak.pl --seqs 100 $1
cd $1".subfiles"
echo  $1".subfiles"
