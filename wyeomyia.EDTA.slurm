#!/bin/bash
#SBATCH --time=7-96:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=32gb
#SBATCH --partition=Orion

module load anaconda3

conda activate EDTA

perl EDTA/EDTA.pl --genome /projects/cooper_research2/liz/Mosquito/Wyeomyia/new-annotation-2022/wyeomyia.polished.fasta --anno 1 --threads 8 --curatedlib wyeomyia.fasta.mod.EDTA.TElib.fa --sensitive 1

conda deactivate
