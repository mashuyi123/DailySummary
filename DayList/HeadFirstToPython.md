### IDLE使用技巧 ###
1、IDLE使用颜色区分显示代码：内置函数紫色、字符串绿色、关键字橙色、生成结果蓝色。

2、键入一些代码，TAB键，代码建议或补全。

### python基本语法 ###
1、python的变量标识符没有类型。

2、python列表

python列表是一个数据集合，数据项之间用逗号分隔，整个列表用中括号包围。

	python中创建一个列表，解释器会在内存中创建一个类似数组的数据结构来存储数据，数据项自下而上堆放，形成堆栈。
	listA.append("foot") //在列表末尾增加数据
	listA.pop() //在列表末尾删除数据
	listA.extend(["book","drink"]) //在列表中追加一个列表
	listA.remove("book") //在列表中删除某一特定项目
	listA.insert(0,"bread") //在某个特定位置前增加一个数据
	len(listA) //可以统计列表中数据项的个数

3、使用while和for都是为了处理迭代结构的数据，但是while使用时要有状态信息（count）,for循环由python解释器考虑状态信息。

4、isinstance() 允许检查某个特定标识符是否包含某个特定类型的数据，eg: isinstance(names,list)，返回true。

	python中有70多个BIF（内置函数），在IDE shell中，键入dir(__builtins__)可以看到python提供的内置方法列表；
	小写单词都是BIF，查看某个BIF功能。在shell中键入help(input)，就能得到确切BIF功能描述。
![](https://i.imgur.com/R2IdIjm.png)

5、用IDLE执行模块，导入文件后，按F5调用即可。
![](https://i.imgur.com/wRjTNab.png)

6、发布模块到本地副本
	
- 为模块创建一个文件夹，并把代码放在里面；
- 在新文件夹中国创建一个名为"setup.py"的文件，该文件包含发布相关的元数据，也放在创立的文件夹中，如图：

![](https://i.imgur.com/yWT9ooJ.png)

- 发布：完成后模块已经转换为发布，安装在本地副本上。

		python setup.py sdist
		python setup.py install (linux环境中：sudo python3 setup.py install）
	
![](https://i.imgur.com/4oKWEqa.png)
![](https://i.imgur.com/ryCZXPt.png)

- 导入模块就可以使用了：import nester

		使用模块时要注意命名空间的问题，命令空间就像是姓氏；
		在某个命名空间中想指示另外一个模块命名空间中的某个函数，就需要用该模块的命名空间对这个函数的调用做出限定。
7、python常用BIF

	range() //返回一个迭代器，根据需要生成一个指定范围的数字
	enumerate() //创建成对数据的一个编号列表，从0开始
	id() //返回一个python数据对象的唯一标识
	next() //返回一个可迭代数据对象如列表的下一项eg:range(3)生成0/1/2
	
