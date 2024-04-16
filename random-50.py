ortho_groups = []
with open("scos-all.txt") as fh:
	for line in fh:
		line = line.strip("\n")
		line = line.split("  ")
		for group in line:
			ortho_groups.append(group)

fh.close()

total_groups = len(ortho_groups)

import random

randNums = []

while len(randNums) < 50:
	r = random.randint(0,total_groups-1)
	if r not in randNums:
		randNums.append(r)
	else:
		continue

OG_list = []
for number in randNums:
	orthogroup = ortho_groups[number]
	OG_list.append(orthogroup)

print(OG_list)
print(len(OG_list))

