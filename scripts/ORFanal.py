#!/software/bin/python2.7
#Premier programme a lancer apres scriptENCprime.sh 
#ORFanal Cystodites_dellechiajei_purple#solo200.orf Cystodites_dellechiajei_purple#solo200.cov
#ressort un tableau avec des statistiques descriptives calculees sur le fichier '*.orf' 
import sys
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqUtils import GC123
input=sys.argv[1]				#nom du fichier 'orf' de PopPhyl
if(input.find("help")>=0):
        print("ORFanal Cystodites_dellechiajei_purple#solo200.orf Cystodites_dellechiajei_purple#solo200.cov")
        sys.exit()

coverageFile=sys.argv[2]			#nom du fichier contenant les valeurs de couvertures
output="locus\tLtot\tL12\tL3\tcov\tGCtot\tGC12\tGC3\t"

table=["TTT", "TTC", "TTA", "TTG", "TCT", "TCC", "TCA", "TCG", "TAT", "TAC", "TAA", "TAG", "TGT", "TGC", "TGA", "TGG", "CTT", "CTC", "CTA", "CTG", "CCT", "CCC", "CCA", "CCG", "CAT", "CAC", "CAA", "CAG", "CGT", "CGC", "CGA", "CGG", "ATT", "ATC", "ATA", "ATG", "ACT", "ACC", "ACA", "ACG", "AAT", "AAC", "AAA", "AAG", "AGT", "AGC", "AGA", "AGG", "GTT", "GTC", "GTA", "GTG", "GCT", "GCC", "GCA", "GCG", "GAT", "GAC", "GAA", "GAG", "GGT", "GGC", "GGA", "GGG"]
for cod in table:
	output=output+"{} ".format(cod)
output=output+"\n"

CodonCount="Contigs\t{}\n".format(" ".join(table))
acgtfreq="Nucleotide f_A f_C f_G f_T\n"

def countCodons(sequence, table):
	tmp=[]
	res=[]
	for pos in range(0, len(sequence), 3):
		tmp.append(sequence[pos:(pos+3)])
	for cod in table:
#		res=res+"{} ".format(tmp.count(cod))
		res.append(tmp.count(cod))
	return(res)

coverage={}
readCoverage=open(coverageFile, "r")		#ouvre le fichier de couverture
for j in readCoverage:
	j=j.strip().split("\t")
	coverage[j[0]]=int(j[1])
readCoverage.close()

nlocus=0
codonsTot=[0]*len(table)
nA=0.0
nC=0.0
nG=0.0
nT=0.0
for i in SeqIO.parse(input, "fasta"):
	nlocus+=1
	if(len(i.seq)%3!=0):			#garde une sequence de longueur multiple de 3
		while(len(i.seq)%3!=0):
			i.seq=i.seq[:-1]
	Ltot=len(i.seq)
	L12=len(i.seq[::3]+i.seq[1::3])
	L3=len(i.seq[2::3])
	
	gctot=GC(i.seq)
	gc12=GC(i.seq[::3]+i.seq[1::3])
	gc3=GC(i.seq[2::3])
	
	fA=i.seq.count("A")/float(Ltot)
	fC=i.seq.count("C")/float(Ltot)
	fG=i.seq.count("G")/float(Ltot)
	fT=i.seq.count("T")/float(Ltot)
	
	nA=nA+fA
	nC=nC+fC
	nG=nG+fG
	nT=nT+fT
	couverture=coverage.get(i.id)
	
	codons=countCodons(sequence=str(i.seq), table=table)
	codonsTot=[a+b for a,b in zip(codonsTot, codons)]	
	codons=" ".join("{0}".format(n) for n in codons)
	CodonCount=CodonCount+"{} {}\n".format(i.id, codons)
	acgtfreq=acgtfreq+"{} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(i.id, fA, fC, fG, fT)

	output=output+"{}\t{}\t{}\t{}\t{}\t{:.6f}\t{:.6f}\t{:.6f}\t{}\n".format(i.id, Ltot, L12, L3, couverture, gctot, gc12, gc3, codons)

file=open("statsDescriptives_ORF.out", "w")
file.write(output)
file.close()

codonsTot=" ".join("{0}".format(n) for n in codonsTot)
#CodonCount="{}\n{}\n".format(nlocus, len(table))+CodonCount+"Totals> {} ".format(codonsTot)
file=open("CodonCount.codcnt","w")
file.write(CodonCount)
file.close()

acgtfreq=acgtfreq+"Totals> {:.6f} {:.6f} {:.6f} {:.6f} ".format(nA/nlocus, nC/nlocus, nG/nlocus, nT/nlocus)
file=open("BaseFreq.acgtfreq", "w")
file.write(acgtfreq)
file.close()

