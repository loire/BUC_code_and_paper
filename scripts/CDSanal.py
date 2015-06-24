#!/software/bin/python2.7
#CDSanal Cystodites_dellechiajei_purple#solo200.cds Cystodites_dellechiajei_purple#solo200.cov
#ressort un tableau avec des statistiques descriptives calculees sur le fichier '*.cds'
import sys
from Bio import SeqIO
input=sys.argv[1]
if(input.find("help")>=0):
	print("CDSanal Cystodites_dellechiajei_purple#solo200.cds Cystodites_dellechiajei_purple#solo200.cov")
	sys.exit()

coverageFile=sys.argv[2]

def mangeTonU(contig, coverage):
	res=""
	for i in range(0, len(contig[contig.keys()[0]]), 1):	#boucle le long des positions
		posTmp=[]
		for j in  contig: 				#boucle le long des contigs
			posTmp.append(contig[j][i])
		nA=posTmp.count("A")
		nT=posTmp.count("T")
		nC=posTmp.count("C")
		nG=posTmp.count("G")
		
		nNuc=nA+nT+nC+nG

		nN=posTmp.count("N")
		nMissing=posTmp.count("-")
		cov=coverage.get(contig.keys()[0].split("|")[0])
		if(i%3==0):
			pos="pos1"
		if(i%3==1):
			pos="pos2"
		if(i%3==2):
			pos="pos3"
		if(nA != nNuc and nT != nNuc and nC != nNuc and nG != nNuc and nN < (len(posTmp)-4) and nMissing !=len(posTmp)):
			res=res+"{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(contig.keys()[0].split("|")[0], cov, len(posTmp), i+1, pos, nA, nT, nC, nG, nN, nMissing)
	return(res)
		
coverage={}
readCoverage=open(coverageFile, "r")            #ouvre le fichier de couverture
for j in readCoverage:
        j=j.strip().split("\t")
        coverage[j[0]]=int(j[1])
readCoverage.close()


alignment={}
for i in SeqIO.parse(input, "fasta"): #dictionnaire contenant des alignements qui sont eux memes des dictionnaires de sequences
	name=i.id.split("|")[0]
	if name not in alignment:
		alignment[name]={}
		alignment[name][i.id]=str(i.seq)
	else:
		alignment[name][i.id]=str(i.seq)

output="contig\tcov\tnIndiv\tpos\tsite\tnA\tnT\tnC\tnG\tnN\tnMissing\n"
for i in alignment:
	output=output+"{}".format(mangeTonU(alignment[i], coverage))

file=open("statsDescriptives_CDS.out", "w")
file.write(output)
file.close()



