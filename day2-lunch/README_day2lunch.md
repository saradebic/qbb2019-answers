
head -40000 ~/qbb-answers/rawdata/SRR072893.fastq > SRR072893.10k.fastq
fastqc SRR072893.10k.fastq
hisat2 -x BDGP6 -U SRR072893.10k.fastq -S stdout.sam
samtools sort -@ 4 stdout.sam > stdout.bam
samtools index stdout.bam
stringtie stdout.bam -G BDGP6.Ensembl.81.gtf -o alignmentSRR -e -B -p 4

cut -f 1 alignmentSRR | sort | uniq -c > chromosomeAlignments.txt #fast way, cut fields to get the 1st column, sort to be able to use unique with a counter 
