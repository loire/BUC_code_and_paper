
data_chelo_gc3_poor <- read.table("Chelo_GC3_poor_contig.txt.fasta.sfs",header=TRUE) 
data_chelo_all <- read.table("DNA_Chelo.fasta.sfs",header=TRUE)               
data_emys_high_cov <- read.table("Emys_high_cov_contig.txt.fasta.sfs",header=TRUE)
data_chelo_gc3_rich <- read.table("Chelo_GC3_rich_contig.txt.fasta.sfs",header=TRUE)
data_emys_all <- read.table("DNA_emys.fasta.sfs",header=TRUE)           
data_emys_low_cov <- read.table("Emys_low_cov_contig.txt.fasta.sfs",header=TRUE)
data_chelo_high_cov <- read.table("Chelo_high_cov_contig.txt.fasta.sfs",header=TRUE)
data_emys_gc3_poor <- read.table("Emys_GC3_poor_contig.txt.fasta.sfs",header=TRUE)
data_chelo_low_cov <- read.table("Chelo_low_cov_contig.txt.fasta.sfs",header=TRUE)
data_emys_gc3_rich <- read.table("Emys_GC3_rich_contig.txt.fasta.sfs",header=TRUE)

pdf("Emys_Chelo_Allele_spectrum.pdf")
par(mfrow=c(2,1), mar=c(4,4,4,4), oma=c(2,2,2,2)) 


barplot(data_chelo_all$nb_SNP_syno_unfolded,names.arg=round(data_chelo_all$GC_allele_frequency/8,3),border = NA, cex.names=0.5,main="Chelonoides nigra",ylab="count")
barplot(data_emys_all$nb_SNP_syno_unfolded,names.arg=round(data_emys_all$GC_allele_frequency/12,3),border = NA, cex.names=0.5,main="Emys orbicularis",xlab="Allele frequency",ylab="count")

mtext("GC alleles frequency spectrum",side=3,outer=T,cex=1.5)


barplot(data_chelo_gc3_poor$nb_SNP_syno_unfolded,names.arg=round(data_chelo_gc3_poor$GC_allele_frequency/8,3),border = NA, cex.names=0.5,main="Chelonoides nigra",ylab="count")
barplot(data_emys_gc3_poor$nb_SNP_syno_unfolded,names.arg=round(data_emys_gc3_poor$GC_allele_frequency/12,3),border = NA, cex.names=0.5,main="Emys orbicularis",xlab="Allele frequency",ylab="count")

mtext("GC alleles frequency spectrum (Low GC3)",side=3,outer=T,cex=1.5)


barplot(data_chelo_gc3_rich$nb_SNP_syno_unfolded,names.arg=round(data_chelo_gc3_rich$GC_allele_frequency/8,3),border = NA, cex.names=0.5,main="Chelonoides nigra",ylab="count")
barplot(data_emys_gc3_rich$nb_SNP_syno_unfolded,names.arg=round(data_emys_gc3_rich$GC_allele_frequency/12,3),border = NA, cex.names=0.5,main="Emys orbicularis",xlab="Allele frequency",ylab="count")

mtext("GC alleles frequency spectrum (high GC3)",side=3,outer=T,cex=1.5)


barplot(data_chelo_low_cov$nb_SNP_syno_unfolded,names.arg=round(data_chelo_low_cov$GC_allele_frequency/8,3),border = NA, cex.names=0.5,main="Chelonoides nigra",ylab="count")
barplot(data_emys_low_cov$nb_SNP_syno_unfolded,names.arg=round(data_emys_low_cov$GC_allele_frequency/12,3),border = NA, cex.names=0.5,main="Emys orbicularis",xlab="Allele frequency",ylab="count")

mtext("GC alleles frequency spectrum (low coverage)",side=3,outer=T,cex=1.5)



barplot(data_chelo_high_cov$nb_SNP_syno_unfolded,names.arg=round(data_chelo_high_cov$GC_allele_frequency/8,3),border = NA, cex.names=0.5,main="Chelonoides nigra",ylab="count")
barplot(data_emys_high_cov$nb_SNP_syno_unfolded,names.arg=round(data_emys_high_cov$GC_allele_frequency/12,3),border = NA, cex.names=0.5,main="Emys orbicularis",xlab="Allele frequency",ylab="count")

mtext("GC alleles frequency spectrum (high coverage)",side=3,outer=T,cex=1.5)

dev.off()
#system("fig2dev -L emf Emys_Chelo_Allele_spectrum.fig > Emys_Chelo_Allele_spectrum.emf")
