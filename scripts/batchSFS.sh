# Adding again something to illustrate branching

# Adding something to a script to test commit 


#~ #!/bin/bash
#~ 
#~ # Chelo_files
#~ 
#~ # All contig
#~ 
#~ Site_frequency_spectra DNA_Chelo.fasta Chelonoidis_nigra Chelonoidis_carbonaria 5 0.5 10 20 0 1 8
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > DNA_Chelo.fasta.sfs
#~ 
#~ 
#~ # GC rich
#~ Site_frequency_spectra Chelo_GC3_rich_contig.txt.fasta Chelonoidis_nigra Chelonoidis_carbonaria 5 0.5 10 20 0 1 8
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > Chelo_GC3_rich_contig.txt.fasta.sfs
#~ 
#~ # GC poor
#~ 
#~ Site_frequency_spectra Chelo_GC3_poor_contig.txt.fasta Chelonoidis_nigra Chelonoidis_carbonaria 5 0.5 10 20 0 1 8
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > Chelo_GC3_poor_contig.txt.fasta.sfs
#~ 
#~ 
#~ # Cov high
#~ 
#~ Site_frequency_spectra Chelo_high_cov_contig.txt.fasta Chelonoidis_nigra Chelonoidis_carbonaria 5 0.5 10 20 0 1 8
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > Chelo_high_cov_contig.txt.fasta.sfs
#~ 
#~ # Cov Low
#~ 
#~ Site_frequency_spectra Chelo_low_cov_contig.txt.fasta Chelonoidis_nigra Chelonoidis_carbonaria 5 0.5 10 20 0 1 8
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > Chelo_low_cov_contig.txt.fasta.sfs
#~ 
#~ 
#~ 
#~ 
#~ 
#~ 
#~ # Emys_files
#~ 
#~ # All contig
#~ 
#~ Site_frequency_spectra DNA_emys.fasta Emys_orbicularis Trachemys_scripta 10 0.5 10 20 0 1 12
#~ 
#~ awk '{print$1,$2}' Site_frequency_spectra_SFS > DNA_emys.fasta.sfs


# GC rich
Site_frequency_spectra Emys_GC_rich.txt.fasta Emys_orbicularis Trachemys_scripta 10 0.5 10 20 0 1 12

awk '{print$1,$2}' Site_frequency_spectra_SFS > Emys_GC3_rich_contig.txt.fasta.sfs

# GC poor

Site_frequency_spectra Emys_GC_poor.txt.fasta Emys_orbicularis Trachemys_scripta 10 0.5 10 20 0 1 12

awk '{print$1,$2}' Site_frequency_spectra_SFS > Emys_GC3_poor_contig.txt.fasta.sfs


# Cov high

Site_frequency_spectra Emys_high_cov.txt.fasta Emys_orbicularis Trachemys_scripta 10 0.5 10 20 0 1 12

awk '{print$1,$2}' Site_frequency_spectra_SFS > Emys_high_cov_contig.txt.fasta.sfs

# Cov Low

Site_frequency_spectra Emys_low_cov.txt.fasta Emys_orbicularis Trachemys_scripta 10 0.5 10 20 0 1 12

awk '{print$1,$2}' Site_frequency_spectra_SFS > Emys_low_cov_contig.txt.fasta.sfs






