##########################################

### this section will find the families with duplicates and only keep the "better" orf
### first specify the output file
fout = open("new-orfs-GA08.fasta","w")

### find the length of the file and the families in the file
headers = []
families = []
lines = 0
with open("cluster-seqs-GA08.fasta.transdecoder.pep","r") as fh:
	for line in fh:
		lines += 1
		if line.startswith(">"):
			family = line.split(".")[0]
			if family not in families:
				families.append(family)

### choose the best ORF for each family and write that to a list
for family in families:
	with open("cluster-seqs-GA08.fasta.transdecoder.pep","r") as fh2:
		count = 0
		length = 0
		score = 0
		famLine = ""
		while count <= lines:
			line = fh2.readline()
			count += 1
			if family in line:
				lineLength = float(line.split("len:")[1].split(" ")[0])
				lineScore = float(line.split("score=")[1].split(" ")[0])
				if lineLength > length:
					length = lineLength	
					score = lineScore
					famLine = line
				elif lineLength == length:
					if lineScore > score:
						score = lineScore
						famLine = line

		headers.append(famLine)

### find the sequences from the headers list and write the header and sequences to a new file
for header in headers:
	with open("cluster-seqs-GA08.fasta.transdecoder.pep","r") as file:
		count2 = 0	
		while count2 <= lines:	
			line = file.readline()
			count2 += 1			
			if header in line:
				orf = line
				while count2 <= lines:
					line = file.readline()
					count2 += 1
					if line.startswith(">"):
						fout.write(orf)
						break
					elif line == "":
						fout.write(orf)
						break
					else:
						orf += line

fout.close()

##########################################

###this section will keep only the headers from the previous file
fout2 = open("new-orf-headers-GA08.txt","w")

with open("new-orfs-GA08.fasta") as file:
	for line in file:
		if line.startswith(">"):
			fout2.write(line)

fout2.close()

##########################################

### this section will only keep the clusters with a 200NT or longer ORF found in it
### first specify the output file
fout3 = open("new-final-clusters-GA08.fa.clstr","w")


### first make a list of all the families that have an ORF
families = []
with open("new-orf-headers-GA08.txt","r") as file:
	for line in file:
		family = line.split(".")[0]
		families.append(family)

### find the length of the file that will be looped through
lines = 0
with open("new-both-2s-400NT.fa.clstr","r") as fh:
	for line in fh:
		lines += 1

### loop through file and only keep clusters with an ORF
with open("new-both-2s-400NT.fa.clstr","r") as fh2:
	count = 0
	line = fh2.readline()
	count += 1
	while count <= lines:
		
		if line.startswith(">"):
			cluster = line
			while count <= lines:
				line = fh2.readline()
				count += 1
				if line.startswith(">"):
					for family in families:
						if family in cluster:
							fout3.write(cluster)
							break
					break
				elif line == "":
					for family in families:
						if family in cluster:
							fout3.write(cluster)
							break
					break
				else:
					cluster += line
		else:
			line = fh2.readline()
			count += 1
fout3.close()

##########################################

### this section will find the sequences that correspond to the final clusters
### first specify the output file
fout4 = open("new-final-cluster-seqs-GA08.fasta","w")

### make a list of the headers in the final clusters
headers = []
with open("new-final-clusters-GA08.fa.clstr","r") as fh:
	for l in fh:
		if l.startswith(">"):
			continue
		else:
			l = l.split(", ")[1]
			l = l.split(".")[0]
			if l not in headers:
				headers.append(l)

### write all the sequences that belong to those headers to the output file
with open("all-species.fa","r") as file:
	match = False
	wholeLine = ""
	for line in file:
		if line.startswith(">"):
			if match == True:
				fout4.write(wholeLine)
				wholeLine = ""
			if match == False:
				wholeLine = ""
			header = line.split(" ")[0]
			if header in headers:
				wholeLine += line
				match = True
			elif header not in headers:
				match = False
		elif line == "":
			if match == True:
				fout4.write(wholeLine)
				wholeLine = ""
		else:
			wholeLine += line
	if match == True:
		fout4.write(wholeLine)
fout4.close()

##########################################

### this section will filter the duplicate species found in clusters
### then refilter based on 2s and ORF requirements because these may no longer be satisfied

### first specify the output file
fout5 = open("vhica-clusters-GA08.fa.clstr","w")

### first find length of file that will be looped through
lines = 0
with open("final-clusters-GA08.fa.clstr","r") as file:
	for line in file:
		lines += 1

### create a dictionary of the families with ORFs 
### key is family header, values are the ORF length and the ORF score
families = {}
with open("orf-headers-GA08.txt","r") as file:
	for line in file:
		family = line.split(".")[0]
		length = float(line.split("len:")[1].split(" ")[0])
		score = float(line.split("score=")[1].split(" ")[0])
		families[family] = [length,score]

### loop through clusters file using determined length
### find the clusters that contain more than one species
### compare the lines and keep only the "better" line
### only keep the cluster if there is more than one species
### prioritize ORFs over sequences with no ORF
with open("final-clusters-GA08.fa.clstr","r") as fh2:
	line = fh2.readline()
	count = 1
	while count <= lines:

		if line.startswith(">"):
			cluster = line
			species_lines = {}

			while count <= lines:
				line = fh2.readline()
				count += 1

				if line.startswith(">"):
					entries = 0
					for mosquito,entry in species_lines.items():
						entries += 1
						cluster += entry
					if entries > 1:
						fout5.write(cluster)
					break

				elif line == "":
					entries = 0
					for mosquito,entry in species_lines.items():
						entries += 1
						cluster += entry
					if entries > 1:
						fout5.write(cluster)
					break

				else:
					species = line.split(">")[1].split("_")[0]
					
					if species not in species_lines.keys():
						species_lines[species] = line
					else:
						current_line = species_lines[species]
						current_family = current_line.split(", ")[1].split(".")[0]
						current_length = float(current_line.split("\t")[1].split("nt")[0])
						if current_family in families:
							current_orf = 1
						elif current_family not in families:
							current_orf = 0

						new_length = float(line.split("\t")[1].split("nt")[0])
						new_family = line.split(", ")[1].split(".")[0]
						if new_family in families:
							new_orf = 1
						elif new_family not in families:
							new_orf = 0

						if new_orf > current_orf:
							species_lines[species] = line
						
						elif new_orf == current_orf:
							if new_orf == 0:
								if new_length > current_length:
									species_lines[species] = line

							elif new_orf == 1:
								current_orf_length = families[current_family][0]
								current_orf_score = families[current_family][1]

								new_orf_length = families[new_family][0]
								new_orf_score = families[new_family][1]

								if new_orf_length > current_orf_length:
									species_lines[species] = line

								elif new_orf_length == current_orf_length:
									if new_orf_score > current_orf_score:
										species_lines[species] = line



fout5.close()

##########################################

### this section creates a file for each of the clusters

### first loop through the vhica cluster seqs file and find the length
lines = 0
with open("vhica-cluster-seqs-GA08.fasta","r") as fh1:
	for line in fh1:
		lines += 1

### then loop through the vhica cluster file and produce a file per cluster
with open("vhica-clusters-GA08.fa.clstr","r") as file:
	cluster_header = None

	for line in file:
		if line.startswith(">"):
			if cluster_header:
				fout = open(cluster_header,"w")
				fout.write(cluster_seqs)
				fout.close()

			cluster = line.split(" ")[1].split("\n")[0]
			cluster_header = "cluster_" + cluster + ".fa"
			cluster_seqs = ""

		else:
			family = line.split(", ")[1].split(".")[0]

			with open("vhica-cluster-seqs-GA08.fasta","r") as fh:
				count = 0
				match = False

				while count <= lines:
					line1 = fh.readline()
					count += 1

					if match == True:
						break

					elif line1.startswith(family):
						cluster_seqs += line1

						while count <= lines:
							line1 = fh.readline()
							count += 1

							if line1.startswith(">"):
								match = True
								break

							else:
								cluster_seqs += line1

					else:
						continue


	if cluster_header:
		fout = open(cluster_header,"w")
		fout.write(cluster_seqs)
		fout.close()

##########################################
