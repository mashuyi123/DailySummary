## python下载安装BeautifulSoup库 ##

1. 下载地址：[https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/ "https://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/")

2. 将下载的文件解压到python安装目录下：
![](https://i.imgur.com/hg6uvw4.png)
3. 进入cmd，切换到文件解压目录：
![](https://i.imgur.com/52pwOh6.png)
4. 依次执行：

	python setup.py build 
    python setup.py install
5. 检查是否安装成功：

	import bs4 from bs4 import BeautifulSoup  
## python安装Request模块 ##
1. 使用cmd进入python安装目录下的Scripts文件夹，在命令行中输入pip install requests，等待安装完成即可。
![](https://i.imgur.com/jGOVUwA.png)
![](https://i.imgur.com/wmOUTwD.png)


2. 如果安装报错，检查是否开着代理，关掉代理再试下~~~
![](https://i.imgur.com/dw51LTT.png)
