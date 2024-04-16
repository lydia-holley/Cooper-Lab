
### script to remove clusters with only one species and sequences less than 400NT

### this section removes sequences that are less than 400NT
### first open original file and loop through, only write long enough sequences to the new file
fout = open("new-length-400NT.fa.clstr","w")
with open("reduced-all.fa.clstr","r") as file:
	for line in file:
		if line.startswith(">"):
			fout.write(line)
			continue
		else:
			right = line.split("\t")[1]
			size = right.split("n")[0]
			size = int(size)
			if size >= 400:
				fout.write(line)
				continue
			else:
				continue
fout.close()

### this section removes clusters with only one species
### first find the number of lines in the current file and open new file
fout2 = open("new-both-2s-400NT.fa.clstr","w")
with open("new-length-400NT.fa.clstr","r") as fh:
	length = 0
	for i in fh:
		length += 1

### then loop through the current file and remove the entries that only have one species
with open("new-length-400NT.fa.clstr","r") as fh1:
	line = fh1.readline()
	lines = 1
	while lines <= length:
		if line.startswith(">"):
			count = 0
			while count < 25:
				nextline = fh1.readline()
				lines += 1
				if nextline == "":
					if count > 1:
						fout2.write(line)
					count = 0
					break
				elif not nextline.startswith(">"):
					count += 1
					line += nextline
				elif nextline.startswith(">"):
					if count > 1:
						fout2.write(line)
					line = nextline
					count = 0
					break
fout2.close()

### this section will find the corresponding sequences for each of the kept cluster seqs: need this for transdecoder
### first open the reduced file and keep the headers in a list to use in the next step
fout3 = open("new-cluster-seqs-GA08.fasta","w")

headers = []
with open("new-both-2s-400NT.fa.clstr","r") as fh:
	for l in fh:
		if l.startswith(">"):
			continue
		else:
			l = l.split(", ")[1]
			l = l.split(".")[0]
			headers.append(l)

### then write all the sequences that are in the chose clusters into the new sequences file
with open("all-species.fa","r") as file:
	match = False
	wholeLine = ""
	for line in file:
		if line.startswith(">"):

			if match == True:
				fout3.write(wholeLine)
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
				fout3.write(wholeLine)
				wholeLine = ""

		else:
			wholeLine += line

	if match == True:
		fout3.write(wholeLine)

fout3.close()
