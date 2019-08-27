#!/bin/bash

GENOME=~/data/genomes/BDGP6.fa
ANNOTATION=~/data/genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ~/data/rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p $THREADS -x BDGP6 -U $SAMPLE.fastq -S $SAMPLE.stdout.sam
  samtools sort -@ $THREADS $SAMPLE.stdout.sam > stdout.bam
  samtools index stdout.bam
  stringtie stdout.bam -G $ANNOTATION -o $SAMPLE_alignment -e -B -p 4
done