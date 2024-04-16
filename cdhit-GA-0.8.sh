#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128gb
#SBATCH --time=72:00:00
#SBATCH --partition=Orion

module load cd-hit
cd-hit-est -i all-species.fa -o reduced-all.fa -d 0 -M 1200 -T 16 -G 1 -g 1 -c 0.8 -aS 0.8 -n 5 

