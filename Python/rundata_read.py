import os

# os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter5")
os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter5")

# 打开文件读取数据的函数
sarah = []
def readData(fileName):
	try:
		with open(fileName) as readFile:
			data = readFile.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

james = readData('james.txt')
julie = readData('julie.txt')
mikey = readData('mikey.txt')
sarah = readData("sarah.txt")


# 函数用来过滤'-'和':'不标准的字符串数据
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'	
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' +secs)

jamesData = []
julieData = []
mikeyData = []
sarahData = []

jamesData = print(sorted(set([sanitize(each) for each in james]))[0:3])
julieData = print(sorted(set([sanitize(each) for each in julie]))[0:3])
mikeyData = print(sorted(set([sanitize(each) for each in mikey]))[0:3])
sarahData = print(sorted(set([sanitize(each) for each in sarah]))[0:3]) 
