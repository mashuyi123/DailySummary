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
finally:
	# 文件不存在时，创建data文件对象会失败,data.close()会报错，提示NameError,data找不到
	if "data" in locals():
		data.close()

try:
	with open("man_data.txt","w") as print_man:
		print(man,file = print_man)
	with open("other_data.txt","w") as print_other:
		print(other,file = print_other)
except IOError:
	print("File error!")

with open("man_data.txt") as mdf:
	print(mdf.readline())


aaa = "mmashuyitestaaa"

if "mashuyi" in aaa:
	print("a")