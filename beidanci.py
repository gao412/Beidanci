# coding = utf-8
import random
import os
import sys

file = "wordlist.txt"
filename = os.getcwd() + "/" + "wordlist.txt"
wl = os.getcwd() + "/" + "wordneetreview.txt"

class BeiDanCi(object):
	def __init__(self, dictionary):
		file_dir = os.path.split(filename)[0]
		if not os.path.exists(file_dir):
			os.makedirs(file_dir)
		if not os.path.exists(filename):
			os.system(r'touch %s' % filename)
		self.dictionary = open(filename, "a+") # a+表示读取和追加写入模式

	def showlist(self, num):
		self.dictionary.seek(0) # 由于是a+打开文件，因此需要用这句代码把指针调到最开始
		# number = num + 1
		line = self.dictionary.readlines()
		try:
			numbers = random.sample(range(0, len(line) + 1), num)
			# line = line[: num]
			# for l in line:
			# 	l = l.strip('\n')
			# 	print(l)
			for m in numbers:
				w = line[m].strip('\n')
				print(w)
			# for line in self.dictionary.readlines(number):
			# 	line = line.strip('\n')
			# 	print(line)
		except:
			print("数量超出词库范围，请重新输入")
			
	def addword(self):
		a = input("请输入单词：")
		b = input("请输入词性：")
		c = input("请输入意思：")
		word = a + '  ' + b + '  ' + c
		self.write(self.dictionary, word)
		msgbox = '%s has been added into the wordlist' %word
		return msgbox

	def write(self, dic, str):
		str1 = dic.write(str + '\n')
		dic.flush() # 这句代码可以使得文件写入一次保存一次

	def review(self):
		self.dictionary.seek(0)
		wordlist = self.dictionary.readlines()
		flag = 1
		try:
			while(flag): # 先通过随机数获取一个单词，然后用随机数确定模式
				number = random.randint(1,len(wordlist)) 
				word = wordlist[number].split('  ') # 这两行代码是用来获取单词的
				mode = random.randint(0, 1) # 随机确定一种模式
				if mode == 1: # 本程序假设，随机数为1时，模式为英译汉
					hint = "是否认识这个词(y/n)?"
					print(word[0])
					i = input(hint)
					if i == "y" or i == "Y":
						continue
					elif i == "n" or i == "N":
						translate = word[1] + ' ' + word[2]
						print(translate)
					else:
						print("输入有误")
				else:
					hint2 = "请写出这个单词:"
					showword = word[1] + ' ' + word[2]
					print(hint2)
					b = input(showword)
					if b == word[0]:
						print("答对了，继续！")
					else:
						print("错误，正确的意思为：\n" + word[0])
				a = input("继续学习？(y/n)")
				if a == "y" or a == "Y":
					continue
				elif a == "n" or a == "Y":
					break
				else:
					print("输入有误")
		except:
			print("软件出现异常")

			# number = random.randint(1,len(wordlist))
			# word = wordlist[number].split(' ')[0]
			# hint = "是否知道这个词(y/n)?"
			# print(word)
			# i = input(hint)
			# if i == "n" or i == "N":
			# 	a = input("显示意思并展示下一个词？(y/n)")
			# 	if a == "y" or a == "Y":
			# 		print(wordlist[number].split(' ')[1] + ' ' + wordlist[number].split(' ')[2])
			# 	else:
			# 		break
			# else:
			# 	print(wordlist[number].split(' ')[1] + ' ' + wordlist[number].split(' ')[2])

	def ifwordexist(self, word):
		self.dictionary.seek(0)
		line = self.dictionary.readlines()
		flag = 0
		lst = []
		for i in line:
			i = i.split('  ')[0] # 这里用空格作为分隔是因为之前添加word的时候中间空了
			lst.append(i)
		try:
			where = lst.index(word)
			i = input("此单词已存在，是否查看？(y/n)")
			if i == "y" or i == "Y":
				print(line[where])
		except:
			print("开始添加")
			self.addword()
		
		# for l in lst:
		# 	if l == word:
		# 		flag = 1
		# if flag = 1:
		# 	i = input("此单词已存在，是否查看？(y/n)")
		# 	if i == "y" or i == "Y":
		# 		lst.
		# else:
		# 	self.addword()

def menu():
	print("_____________________________________")
	print("欢迎使用本软件")
	print("1.复习单词")
	print("2.添加生词")
	print("3.展示单词列表") # 这个需要一个参数num来确定展示多少个
	print("4.关闭软件")

if __name__ == "__main__":
	beidanci = BeiDanCi(filename)
	while(True):
		menu()
		x = input("请选择序号：")
		if x == "1":
			beidanci.review()
		elif x == "2":
			w = input("请输入您想添加的单词：")
			beidanci.ifwordexist(w)
		elif x == "3":
			i = int(input("请输入查看的单词数量："))
			beidanci.showlist(i)
		elif x == "4":
			print("感谢使用")
			beidanci.dictionary.close()
			sys.exit()
		else:
			print("输入有误")

		c = input("返回主菜单(y) or 退出软件(n)")
		if c == "y" or c == "Y":
			continue
		else:	
			print("感谢使用")
			beidanci.dictionary.close()
			sys.exit()




"""
a = {}
f = 1
def addword():
	n = input("请输入这个单词：")
	x = input("请输入中文意思：")
	a[n] = x

def showall():
	print(a)

def show():
	print("1.查询所有的单词")
	print("2.添加单词")
	print("3.查询特定的单词")

def specialword():
	n = input("请输入这个单词：")
	if n in a.keys():
		print(a.get(n))
	else:
		print("没有这个单词")
		addword()

def review():
	print(random.sample(a.keys(),1))

while(f):
	show()
	x = input("请选择序号：")
	if x == "1":
		showall()
	elif x == "2":
		addword()
	elif x == "3":
		specialword()
	else:
		print("输入有误")
	c = input("是否继续？(y/n):")
	if c == "y" or c == "Y":
		f = 1
	else:
		f = 0

review()

"""








