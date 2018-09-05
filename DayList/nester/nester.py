'''nester.py模块，提供一个print_lol()函数，该函数用户打印列表，其中有可能包含，也可能不包含嵌套列表。'''

def print_lol(the_list,level):
	'''这个函数取一个位置参数，名为"the_list"，可以是任何python列表，也可以是包含嵌套列表的列表，列表的每个数据项会打印到屏幕上，各占一行'''
	for item in the_list:
		if isinstance(item,list):
			print(item)
		else:
			for tab_stop in range(level):
				print("\t",end = "")
			print(item)
