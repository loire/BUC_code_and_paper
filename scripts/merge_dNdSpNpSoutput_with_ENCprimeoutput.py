#!/usr/bin/python

import os,sys
popfile=open(sys.argv[1])
popdat={}
#~ 
#~ 
#~ for line in popfile:
	#~ c=line.split()
	#~ for i in xrange(len(c)):
		#~ print i,c[i]
	#~ sys.exit()


for line in popfile:
	c=line.split()
	if c[1]=="OK":
		if float(c[34])==-1 or float(c[35])==-1:
			popdat[c[0]]=c[33]+" NA NA NA"
		else:
			if float(c[35])!=0:
				pnps=float(c[34])/float(c[35])
			else:
				pnps=0
			popdat[c[0]]=c[33]+" "+c[34]+" "+c[35]+" "+str(pnps)

datafile=open(sys.argv[2])

print "Contig GC3 pn ps pnps ENC ENCprime GC Coverage"
for line in datafile:	
		c=line.split()
		string=" "
		for i in c[1:]:
			string+=i+" "
		if c[0] in popdat:
			print c[0],popdat[c[0]],string


