#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --partition=Orion

for file in files_for_vhica/*.fa
	do
		java -jar macse_v0.9b1.jar -i $file -o output/$file-out.fasta
	done
