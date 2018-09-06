import os
os.getcwd()
os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter3")
# os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter3")
os.getcwd()

man = []
other = []
try:	
	data = open("sketch.txt")
	for each_line in data:
		try:
			(role,line_spoken) = each_line.split(":",1)
			line_spoken = line_spoken.strip()
			if role == "Man":
				man.append(line_spoken)
			elif role == "Other Man":
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print("sketch.txt is missing!")

try:
	print_man = open("man_data.txt","w")
	print(man,file = print_man)
	print_other = open("other_data.txt","w")
	except IOError:
	print("File error!")
finally:
	print_man.close()
	print_other.close()
