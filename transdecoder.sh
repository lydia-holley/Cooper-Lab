#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128gb
#SBATCH --time=72:00:00
#SBATCH --partition=Orion

/projects/cooper_research/Programs/TransDecoder-TransDecoder-v5.5.0/TransDecoder.LongOrfs -t cluster-seqs-GA08.fasta -m 200

/projects/cooper_research/Programs/TransDecoder-TransDecoder-v5.5.0/TransDecoder.Predict -t cluster-seqs-GA08.fasta

