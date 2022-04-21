from sys import argv

_, blank_file_name, output_file_name = argv

output_file = open(output_file_name, "w", encoding="utf8")

for i, line in enumerate(open(blank_file_name, "r", encoding="utf8")):

	if line == "":
		break
		
	if line.startswith("#"):
		output_file.write(line)
		continue
	
	new_line = line[0:-4]
	
	output_file.write(new_line + "\n")

output_file.close()
