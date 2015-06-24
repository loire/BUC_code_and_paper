#!/software/bin/python2.7
#UTRanal Cystodites_dellechiajei_purple#solo200.utr3 Cystodites_dellechiajei_purple#solo200.utr5 Cystodites_dellechiajei_purple#solo200.cov
#ressort un tableau avec des statistiques descriptives calculees sur le fichier '*.utr3' et '*.utr5'
import sys
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqUtils import GC123
inputUTR3=sys.argv[1]
if(inputUTR3.find("help")>=0):
        print("UTRanal Cystodites_dellechiajei_purple#solo200.utr3 Cystodites_dellechiajei_purple#solo200.utr5 Cystodites_dellechiajei_purple#solo200.cov")
        sys.exit()

inputUTR5=sys.argv[2]
inputCov=sys.argv[3]

def GCcontent(sequence):
	L=sequence.count("A")+sequence.count("T")+sequence.count("C")+sequence.count("G")+0.
	if(sequence.count("N")==len(sequence)):
		return("NA")
	else:
		return(100*(sequence.count("C")+sequence.count("G"))/L)

coverage={}
readCoverage=open(inputCov, "r")            #ouvre le fichier de couverture
for i in readCoverage:
        i=i.strip().split("\t")
        coverage[i[0]]=int(i[1])
readCoverage.close()

UTRtot={}

UTR3={}
for i in SeqIO.parse(inputUTR3, "fasta"):
	name=i.id.split("|")[0]
	nbreN=i.seq.count("N")
	if name not in UTRtot:
		UTRtot[name]=str(i.seq)
	else:
		UTRtot[name]=UTRtot[name]+str(i.seq)
	if name not in UTR3:
		#tmp="{}\t{}\t{}\t{}".format(name, len(i.seq), nbreN, GCcontent(i.seq))
		tmp=[name, len(i.seq), nbreN, GCcontent(i.seq)]
		UTR3[name]=tmp
		oldN=nbreN
	else:
		if(nbreN<oldN):
			#tmp="{}\t{}\t{}\t{}".format(name, len(i.seq), nbreN, GCcontent(i.seq))
			tmp=[name, len(i.seq), nbreN, GCcontent(i.seq)]
			UTR3[name]=tmp
			oldN=nbreN

UTR5={}
for i in SeqIO.parse(inputUTR5, "fasta"):
        name=i.id.split("|")[0]
        nbreN=i.seq.count("N")
        if name not in UTRtot:
                UTRtot[name]=str(i.seq)
        else:
                UTRtot[name]=UTRtot[name]+str(i.seq)
        if name not in UTR5:
                #tmp="{}\t{}\t{}\t{}".format(name, len(i.seq), nbreN, GCcontent(i.seq))
                tmp=[name, len(i.seq), nbreN, GCcontent(i.seq)]
                UTR5[name]=tmp
                oldN=nbreN
        else:
                if(nbreN<oldN):
                        #tmp="{}\t{}\t{}\t{}".format(name, len(i.seq), nbreN, GCcontent(i.seq))
                        tmp=[name, len(i.seq), nbreN, GCcontent(i.seq)]
                        UTR5[name]=tmp
                        oldN=nbreN

out="Contig\tcoverage\tGC_tot\tL_UTR3\tNbreN_UTR3\tGC_UTR3\tL_UTR5\tNbreN_UTR5\tGC_UTR5\n"
for i in coverage:
	if i in UTR3:
		Lutr3=UTR3[i][1]
		nNutr3=UTR3[i][2]
		GCUTR3=UTR3[i][3]
	else:
		Lutr3="NA"
		nNutr3="NA"
		GCUTR3="NA"
	
	if i in UTR5:
		Lutr5=UTR5[i][1]
		nNutr5=UTR5[i][2]
		GCUTR5=UTR5[i][3]
	else:
		Lutr5="NA"
		nNutr5="NA"
		GCUTR5="NA"
	if i in UTRtot:
		GCUTRtot=GCcontent(UTRtot[i])
	else:
		GCUTRtot="NA"
        out=out+"{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(i, coverage.get(i), GCUTRtot, Lutr3, nNutr3, GCUTR3, Lutr5, nNutr5, GCUTR5)
file=open("statsDescriptives_UTR.out", "w")
file.write(out)
file.close()
	
