### IDLE使用技巧 ###
1、IDLE使用颜色区分显示代码：内置函数紫色、字符串绿色、关键字橙色、生成结果蓝色。

2、键入一些代码，TAB键，代码建议或补全。

### python基本语法 ###
1、python的变量标识符没有类型。

2、python列表

	python中创建一个列表，解释器会在内存中创建一个类似数组的数据结构来存储数据，数据项自下而上堆放，形成堆栈。
	listA.append("foot") //在列表末尾增加数据
	listA.pop() //在列表末尾删除数据
	listA.extend(["book","drink"]) //在列表中追加一个列表
	listA.remove("book") //在列表中删除某一特定项目
	listA.insert(0,"bread") //在某个特定位置前增加一个数据

3、使用while和for都是为了处理迭代结构的数据，但是while使用时要有状态信息（count）,for循环由python解释器考虑状态信息。

4、isinstance() 允许检查某个特定标识符是否包含某个特定类型的数据，eg: isinstance(names,list)，返回true。

	python中有70多个BIF，在IDE shell中，键入dir(__builtins__)可以看到python提供的内置方法列表；
	小写单词都是BIF，查看某个BIF功能。在shell中键入help(input)，就能得到确切BIF功能描述。
![](https://i.imgur.com/R2IdIjm.png)

