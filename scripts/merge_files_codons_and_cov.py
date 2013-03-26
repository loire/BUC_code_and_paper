#!/usr/bin/python

import os, sys

file_real_coverage=open(sys.argv[1])
data_real_cov={}
for line in file_real_coverage:
	c=line.split()
	data_real_cov[c[0]]=c[1]

file_mean_coverage=open(sys.argv[2])
data_mean_cov={}
for line in file_mean_coverage:
	c=line.split()
	data_mean_cov[c[0]]=c[1]

file_codon=open(sys.argv[3])
for line in file_codon:
	c=line.split()
	print line[:-1],data_real_cov[c[0]],data_mean_cov[c[0]]



