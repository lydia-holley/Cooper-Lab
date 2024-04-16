#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128gb
#SBATCH --time=72:00:00
#SBATCH --partition=Orion

cat *.fa > /projects/cooper_research2/lydia/Mosquito/TE-consensus/annotations-all.fa
