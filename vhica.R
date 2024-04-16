#load the necesary packages

setwd("/Users/lydiaholley/Documents/CooperLab/vhica")

install.packages("vhica")
library(vhica)

install.packages("seqinr")
library(seqinr)

library(tools)

###########################
#######file creation#######
###########################
#codon bias file

file.create("cbias-families.txt")

#orthologues

files <- list.files(path="/Users/lydiaholley/Documents/CooperLab/vhica/macse/orthologues/vhica_files", pattern="*.fa", full.names=TRUE, recursive=FALSE)

for (file in files){
  data = CUB(file)
  filename = basename(file)
  genename = tools::file_path_sans_ext(filename)
  newline = paste(genename, 'Gene', as.numeric(data['aaeg']), as.numeric(data['aalb']), as.numeric(data['acol']), as.numeric(data['agam']), as.numeric(data['cqui']), as.numeric(data['ctar']), as.numeric(data['wsmi']),sep='\t')
  write(newline,file="cbias-families.txt",append=TRUE)
}

# TEs

tefiles <- list.files(path="/Users/lydiaholley/Documents/CooperLab/vhica/tealignments/all-named/vhica_families/aligned", pattern="*.fasta", full.names=TRUE, recursive=FALSE)

for (file in tefiles){
  data = CUB(file)
  filename = basename(file)
  tename = tools::file_path_sans_ext(filename)
  newline = paste(tename, 'TE', as.numeric(data['aaeg']), as.numeric(data['aalb']), as.numeric(data['acol']), as.numeric(data['agam']), as.numeric(data['cqui']), as.numeric(data['ctar']), as.numeric(data['wsmi']),sep='\t')
  write(newline,file="cbias-families.txt",append=TRUE)
}

#################
#pairwise-divergence file

file.create("div-families.txt")

# orthologues

files <- list.files(path="/Users/lydiaholley/Documents/CooperLab/vhica/macse/orthologues/vhica_files", pattern="*.fa", full.names=TRUE, recursive=FALSE)

for (file in files){
  data = div(file, pairwise = TRUE)
  filename = basename(file)
  genename = tools::file_path_sans_ext(filename)
  for (i in 1:nrow(data)){
    newline = paste(genename,as.numeric(data[i,]['div']),as.character(data[i,]['sp1']),as.character(data[i,]['sp2']),sep='\t')
    write(newline,file="div-families.txt",append=TRUE)
  }
}

#TEs

tefiles <- list.files(path="/Users/lydiaholley/Documents/CooperLab/vhica/tealignments/all-named/vhica_families/aligned", pattern="*.fasta", full.names=TRUE, recursive=FALSE)

for (file in tefiles){
  data = div(file, pairwise = TRUE)
  filename = basename(file)
  tename = tools::file_path_sans_ext(filename)
  for (i in 1:nrow(data)){
    newline = paste(tename,as.numeric(data[i,]['div']),as.character(data[i,]['sp1']),as.character(data[i,]['sp2']),sep='\t')
    write(newline,file="div-families.txt",append=TRUE)
  }
}

###################
#####run vhica#####
###################

vc <- read.vhica(cb.filename='cbias-families.txt',div.filename='div-families.txt')
plot(vc, "aaeg", "wsmi")
title("Aedes aegypti v Wyeomyia smithii")

image(vc,"dongR4",treefile="phylo.nwk",skip.void=FALSE)

image(vc,"gypsy",treefile="phylo.nwk",skip.void=FALSE)

image(vc,"copia",treefile="phylo.nwk",skip.void=FALSE)
