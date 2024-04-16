#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --partition=Orion

for file in 50_OG_NT/*.fa
	do
		java -jar macse_v0.9b1.jar -i 50_OG_NT/$file -o outputs/$file-out.fasta
	done
