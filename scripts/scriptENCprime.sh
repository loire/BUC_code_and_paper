#!/bin/bash
# $1 ORF fasta file
seqfilebreak.pl --seqs 100 $1
cd $1".subfiles"
cp /home/etienne/src/ENCprimeUnix/ENCprime.defaults . 


for i in `ls $1*`
do
SeqCount -c $i 100
SeqCount -n $i 100
ENCprime $i".codcnt" $i".acgtfreq" 1 $i".resultsENCprime" 1
done
#rm $1".All_ENCprime"
for i in `ls *ENCprime` 
do
	grep -v '^Name' $i > tmp
	grep -v '^Totals' tmp | awk '{print $1,$(NF-7),$(NF-6)}'>> $1".All_ENCprime"
done
#rm $1".GC.txt"
for i in `ls *acgtfreq`
do
	grep -v '^Nuc' $i > tmp
	grep -v '^Tot' tmp | awk '{print $1,$(NF-1)+$(NF-2)}' >> $1".GC.txt"
done
# join with GC %
join $1".All_ENCprime" $1".GC.txt" > $1".ENC_ENCprime_GC.txt"

# merge with $2 Coverage file
../merge_files.py ../$2 ../$3 $1".ENC_ENCprime_GC.txt"  > ../$1".ENC_ENCprime_GC_coverage.txt"

 
