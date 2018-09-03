from tkinter import *
import tkinter
from tkinter import messagebox

class display:
	global cuncu, vartext, result, fuhao
	def __init__(self,display):
		self.display = display
	def jia(self):
		cuncu.append(self.display)
		vartext.set( ''.join(cuncu))#将输出内容进行重置
	def tui(self):
		cuncu.pop()
		vartext.set(''.join(cuncu))
	def clear(self):
		cuncu.clear()
		vartext.set('')
		result = None
		fuhao = None
	def find(self):
		findName = vartext.get()
		n = len(findName)
		if findName == '':
			pass
		elif findName.isdigit()== True:
			temp = False
			with open("record.txt", "r") as f2:
				text = f2.readline()
				text_temp = text.split(' ')
				while text:
					if text_temp[0].find(findName) == 0:
						temp1 =  text_temp[1]
						vartext.set(temp1)
						return vartext
					else:
						text = f2.readline()
						text_temp = text.split(' ')
			if temp == False:
				vartext.set('无该用户！！！')
				return vartext
		else:
			temp = False
			with open("record.txt", "r") as f2:
				text = f2.readline()
				text_temp = text.split(' ')
				while text:
					if text_temp[1].find(findName) == 0:
						temp1 =  text_temp[0]
						vartext.set(temp1)
						return vartext
					else:
						text = f2.readline()
						text_temp = text.split(' ')
			if temp == False:
				vartext.set('无该用户！！！')
				return vartext

def add():
	# 下面定义增加信息文件操作
	def addData():
		if v1.get() == '' or v2.get() == '' :
			messagebox.showerror("Q电话本", "信息不全!")
		else:
			# messagebox.askokcancel("New_guys_phone", "您确认增加该联系人吗?")
			if messagebox.askokcancel("Q电话本", "您确认增加该联系人吗?") is True:
				# 下面是进行增加信息文件操作
				with open("record.txt", "a") as f1:
					f1.write("\n")
					f1.write(v1.get())
					f1.write(" ")
					f1.write(v2.get())
	# 下面是增加信息操作的界面化
	# 创建一个顶级容器
	top1 = Toplevel()
	top1.title("增加用户")
	top1.iconbitmap('my48.ico')
	top1.attributes("-alpha", 0.9)  # 窗口透明度60 %
	addPhoto = PhotoImage(file="bg.gif")  # 创建背景图
	addZhuLabel = Label(top1, image=addPhoto)
	addZhuLabel.pack()
	addTextLabel2 = Label(top1, text="请填入下面信息")
	addTextLabel2.place(relx=0.5, rely=0.2, anchor='center')
	# 创建文本输入框
	v1 = StringVar()
	v2 = StringVar()
	Label(top1, text="电话").place(relx=0.2, rely=0.3)
	e1 = Entry(top1, textvariable=v1)
	e1.place(relx=0.4, rely=0.3, width=70)
	Label(top1, text="姓名").place(relx=0.2, rely=0.5)
	e2 = Entry(top1, textvariable=v2)
	e2.place(relx=0.4, rely=0.5, width=70)
	# 创建选择按钮
	button1 = Button(top1, text='确认', width=5, height=2,  command=addData)
	button1.place(relx=0.2, rely=0.7)
	button2 = Button(top1, text='退出', width=5, height=2, command=top1.withdraw)
	button2.place(relx=0.6, rely=0.7)
	mainloop()

def delete():
	def deleteData():
		deleteName = vv.get()
		if deleteName == '':
			messagebox.showerror("Q电话本", "号码不能为空!")
		else:
			if messagebox.askokcancel("Q电话本", "您确认删除该联系人吗?") is True:
				temp = False
				with open("record.txt", "r") as f5:
					text = f5.readline()
					while text:
						if text.find(deleteName) == 0:
							file_data = ""
							with open("record.txt", "r") as f:
								for line in f:
									if deleteName in line:
										line = line.replace(text[0:len(text)], "")
										# line = line.strip('\n')
									file_data += line
							with open("record.txt", "w") as f:
								f.write(file_data)

							if messagebox.showinfo("Q电话本", "操作成功") == 'ok':
								# exit()
								temp = True
								break
						else:
							text = f5.readline()
				if temp == False:
					messagebox.showerror("Q电话本", "没有该联系人，点击返回")
	top4 = Toplevel()
	top4.title("删除用户")
	top4.iconbitmap('my48.ico')
	top4.attributes("-alpha", 0.9)  # 窗口透明度60 %
	addPhoto = PhotoImage(file="bg.gif")  # 创建背景图
	addZhuLabel = Label(top4, image=addPhoto)
	addZhuLabel.pack()
	deleteTextLabel2 = Label(top4, text="删除的联系人:")
	deleteTextLabel2.place(relx=0.5, rely=0.3, anchor='center')
	# 创建文本输入框
	vv = StringVar()
	Label(top4, text="号码：").place(relx=0.2, rely=0.5)
	e1 = Entry(top4, textvariable=vv)
	e1.place(relx=0.4, rely=0.5, width=70)
	# 创建选择按钮
	button1 = Button(top4, text='确认', width=5, height=2,  command=deleteData)
	button1.place(relx=0.2, rely=0.7)
	button2 = Button(top4, text='返回', width=5, height=2,  command=top4.withdraw)
	button2.place(relx=0.6, rely=0.7)
	mainloop()

def layout(root):
	#显示窗口
	entry1 = tkinter.Entry(root,  textvariable=vartext,bg='Honeydew')
	# entry1.grid(row=0, columnspan=4)
	entry1.place(relx=0.03, width=210, height=42,rely=0.03)
	entry1.bind('<Key-Return>',display.find)
	#第一行按钮
	button750=tkinter.Button(root,text='010',width=6,bg='PaleGreen',command=display('010').jia)
	button751 = tkinter.Button(root, text='011', width=6,bg='PaleGreen',command=display('011').jia)
	button755 = tkinter.Button(root, text='012', width=6,bg='PaleGreen',command=display('012').jia)
	button0 = tkinter.Button(root, text=' 0 ', width=6,bg='PaleGreen',command=display('0').jia)
	button750.place(relx=0.02, rely=0.27)
	button751.place(relx=0.265, rely=0.27)
	button755.place(relx=0.515, rely=0.27)
	button0.place(relx=0.755, rely=0.27)
	# 第二行按钮
	button1 = tkinter.Button(root, text=' 1 ', width=6,bg='PaleGreen',command=display('1').jia)
	button2 = tkinter.Button(root, text=' 2 ', width=6,bg='PaleGreen',command=display('2').jia)
	button3 = tkinter.Button(root, text=' 3 ', width=6,bg='PaleGreen',command=display('3').jia)
	buttonJ = tkinter.Button(root, text=' ← ', width=6,bg='PaleGreen',command=display(' ').tui)
	button1.place(relx=0.02, rely=0.45)
	button2.place(relx=0.265, rely=0.45)
	button3.place(relx=0.515, rely=0.45)
	buttonJ.place(relx=0.755, rely=0.45)
	# 第三行按钮
	button4 = tkinter.Button(root, text=' 4 ', width=6,bg='PaleGreen',command=display('4').jia)
	button5 = tkinter.Button(root, text=' 5 ', width=6,bg='PaleGreen',command=display('5').jia)
	button6 = tkinter.Button(root, text=' 6 ', width=6,bg='PaleGreen',command=display('6').jia)
	buttonE = tkinter.Button(root, text=' Search ', width=6,bg='PaleGreen',command=display('搜索中').find)
	button4.place(relx=0.02, rely=0.63)
	button5.place(relx=0.265, rely=0.63)
	button6.place(relx=0.515, rely=0.63)
	buttonE.place(relx=0.755, rely=0.63)
	# 第四行按钮
	button7 = tkinter.Button(root, text=' 7 ', width=6,bg='PaleGreen',command=display('7').jia)
	button8 = tkinter.Button(root, text=' 8 ', width=6,bg='PaleGreen',command=display('8').jia)
	button9 = tkinter.Button(root, text=' 9 ', width=6,bg='PaleGreen',command=display('9').jia)
	buttonC = tkinter.Button(root, text=' clear  ', width=6, bg='PaleGreen',command=display('').clear)
	button7.place(relx=0.02, rely=0.81)
	button8.place(relx=0.265, rely=0.81)
	button9.place(relx=0.515, rely=0.81)
	buttonC.place(relx=0.755, rely=0.81)

def about():
	top2 = Toplevel()
	top2.title("关于")
	top2.iconbitmap('my48.ico')
	top2.attributes("-alpha", 0.9)  # 窗口透明度60 %
	addPhoto = PhotoImage(file="bg.gif")  # 创建背景图
	addZhuLabel = Label(top2, image=addPhoto)
	addZhuLabel.pack()
	# 不能使用两次Tk（）去创建窗体，因为tkinter中只能有一个主线程，
	# 当你需要再次创建一个窗体时，请使用Toplevel()。
	addTextLabel1 = Label(top2, text="Q_phone_dic(Q电话本)")  # 创建背景图上的文本
	addTextLabel1.place(relx=0.5, rely=0.3, anchor='center')
	addTextLabel2 = Label(top2, text="作者：bc_zhang")
	addTextLabel2.place(relx=0.5, rely=0.5, anchor='center')
	addTextLabel2 = Label(top2, text="版本：version 2.1")
	addTextLabel2.place(relx=0.5, rely=0.7, anchor='center')
	mainloop()

def main():
	# 创建主窗口
	root = Tk()
	root.resizable(0, 0)
	# root.geometry('150x250')
	root.title("Q电话本")
	root.iconbitmap('my48.ico')
	root.attributes("-alpha", 0.9)  # 窗口透明度60 %
	addPhoto = PhotoImage(file="bg.gif")  # 创建背景图
	addZhuLabel = Label(root, image=addPhoto)
	addZhuLabel.pack()
	global cuncu, vartext, result, fuhao
	result = fuhao = None
	vartext = tkinter.StringVar()
	cuncu = []
	layout(root)
	menubar = Menu(root)
	# menubar.add_command(label="Hello!", command=hello)
	menubar.add_command(label='增加', command=add)
	menubar.add_command(label='删除',command=delete)
	menubar.add_command(label='设置')
	menubar.add_command(label='关于',command=about)
	root.config(menu=menubar)
	root.mainloop()

if __name__ == '__main__':
	main()