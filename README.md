# Cooper Lab Repository:
This repository contains scripts I wrote as a graduate research assistant while working for Dr. Elizabeth Cooper's Lab at UNC Charlotte. 
In these scripts I perform a genome annotation and complete all the steps to identify horizontal transfer of transposable elements (TEs) through the vhica R package.

https://elizcooperlab.com

## Genome Annotation
* wyeomyia.EDTA.slurm 

Bash script for de novo TE annotation. Genome fasta file is required for this script.

## VHICA
1. random-50.py

Python script to pick 50 random orthologues from the Single_Copy_Orthologue_Sequences output directory from orthofinder output.

2. macse4orthologues.sh

Bash script to align the sequences in each orthologue file. The 50 random files from the previous step are required for this script

3. concat.sh 

Bash script to combine genome annotations in fasta format for all 7 mosquito species. The genome annotation files are required for this script. 

4. cdhit-GA-0.8.sh

Bash script to cluster the TEs in the combined annotation files using CDHIT. The output from the previous step is required for this script.

5. find-2s-400NT-seqs.py

Python script to do initial filter on cluster output based on number of species and length of sequence. Produces a file with the clusters that meet the criteria and a file containing the corresponding sequences to the kept clusters. The clustered output from the previous step is required for this script

6. transdecoder.sh

Bash script to use transdecoder to identify candidate coding regions. The cluster output from the previous step is required for this script.

7. long-orf-files.py

Python script to filter clusters based on the transdecoder output and produce one file for each cluster that contains the corresponding sequences. The transdecoder output and previously filtered cluster file is required for this script.

8. macse4vhica.sh

Bash script to align the sequence for each cluster file. The output from the previous step is required for this script.

9. vhica.R

R script to determine presence of horizontal transfer of TEs. The outputs from step 2 and step 8 are required for this script.

