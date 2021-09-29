import tkinter as tk

#   可以把GUI用类封装
'''class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()

        self.hi = tk.Button(frame,text='打招呼',fg='blue',command=self.say)
        self.hi.pack(side=tk.LEFT)

    def say(self):
        print('Hello,this is JY_DS')
'''



def test1(): # Label
    def callback():
        var.set('那必须的!')

    root = tk.Tk()
    root.title('Python GUI Test')

    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)

    var = tk.StringVar()
    var.set('春日野穹可不可爱?')

    textlabel1 = tk.Label(frame1,textvariable=var,justify=tk.LEFT)
    textlabel1.pack(side=tk.LEFT)


    photo = tk.PhotoImage(file='img.png')
    imglabel = tk.Label(frame1,image=photo)
    imglabel.pack(side=tk.LEFT)


    Bt = tk.Button(frame2,text='可爱!',command=callback)
    Bt.pack(side=tk.RIGHT)

    frame1.pack(padx=10,pady=10)
    frame2.pack(padx=10,pady=10)
    root.mainloop()

def test2():  # CheckButton复选按钮
    root = tk.Tk()
    gays = ['张xie', '笑宝', '豪豪', 'TJJ']
    v = []

    for gay in gays:
        v.append(tk.IntVar())
        print(v)
        CheckButton = tk.Checkbutton(root, text=gay, variable=v[-1])
        CheckButton.pack(anchor=tk.W)


    root.mainloop()


def test3():  # RadioButton单选按钮
    root = tk.Tk()

    lframe = tk.LabelFrame(root,text='最好的编程语言是？',padx=5,pady=5)
    lframe.pack()

    v = tk.IntVar() # value指选择了按钮后v的值
    langs = [('python', 1), ('java', 2), ('C++', 3), ('rust', 4)]

    for lang, num in langs:
        tk.Radiobutton(lframe, text=lang, variable=v, value=num,indicatoron=False).pack(fill=tk.X)

    root.mainloop()

def test4(): # Entry 文本输入
    def run(): # 验证时调用
        if e1.get() == 'asd':
            return True
        else:
            return False
    def false(): # 验证函数返回false时调用
        print('false调用')

    def show():# 按钮绑定的方法
        print('账号:{}'.format(e1.get()))
        e1.delete(0,tk.END)

        print('密码:{}'.format(e2.get()))
        e2.delete(0,tk.END)

    root = tk.Tk()

    v1 = tk.StringVar()
    v2 = tk.StringVar()

    label1 = tk.Label(root, text='账号')
    label2 = tk.Label(root, text='密码')
    label1.grid(row=0)
    label2.grid(row=1)

    # validate,validatecommand,invalidcommand选项
    e1 = tk.Entry(root, textvariable=v1,validate='focusout',validatecommand=run,invalidcommand=false)
    e2 = tk.Entry(root, textvariable=v2, show='*')
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)

    tk.Button(root,text='确认登录',width=10,command=show).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root,text='退出',width=10,command=root.quit).grid(row=3, column=1, sticky=tk.E, padx=10, pady=5)

    root.mainloop()

def test5():# 简单的计算器实现，使用register包装验证函数
    def calc():
        result = int(v1.get()) + int(v2.get())
        v3.set(result)

    def test(content):
        if content.isdigit():
            return True
        else:
            return False

    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack(padx=10,pady=10)

    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()


    #   当验证设置为key的时候，输入的内容会被拦截到验证函数中
    testCMD = root.register(test)
    tk.Entry(frame,textvariable=v1,width=10,validate='key',validatecommand=(testCMD,'%P')).grid(row=0,column=0)
    tk.Label(frame,text='+').grid(row=0,column=1)
    tk.Entry(frame,textvariable=v2,width=10,validate='key',validatecommand=(testCMD,'%P')).grid(row=0,column=2)
    tk.Label(frame, text='=').grid(row=0, column=3)
    tk.Entry(frame, textvariable=v3, width=10, validate='key', validatecommand=(testCMD, '%P')).grid(row=0, column=4)


    tk.Button(frame,text='计算结果',command=calc).grid(row=1)

    root.mainloop()


def test6():     # listbox组件
    root = tk.Tk()

    listbox = tk.Listbox(root, setgrid=True, height=12)
    listbox.pack()

    lst = ['ZJY', 'ZSJ', 'TJJ', 'RCX']
    for item in lst:
        listbox.insert(tk.END, item)

    tk.Button(root, text='删除', command=lambda x=listbox: x.delete(tk.ACTIVE)).pack()
    root.mainloop()

def test7():    # scrollbar组件 滚动条与其他组件配合使用
    root = tk.Tk()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)    # 滚动列表时 设置滚动条的位置

    for i in range(1, 1000+1):
        listbox.insert(tk.END, str(i))

    listbox.pack(side=tk.LEFT,fill=tk.BOTH)
    scrollbar.config(command=listbox.yview)     # 移动滚动条时，设置列表的位置

    root.mainloop()


def test8():     # scale组件 与滚动条类似，用滚动来表示某个范围内的一个数字
    def show():    # get方法获取位置
        print("scale1的位置{},scale2的位置{}".format(scale1.get(),scale2.get()))

    root = tk.Tk()

    #   resolution控制步长 tickinterval控制刻度,可以不设置
    scale1 = tk.Scale(root,from_=0, to=40, tickinterval=5, length=200, resolution=5, orient=tk.VERTICAL)
    scale1.pack()

    scale2 = tk.Scale(root,from_=0, to=200, tickinterval=20, length=600, resolution=20, orient=tk.HORIZONTAL)    # horizontal水平的
    scale2.pack()

    tk.Button(root,text='获取位置',command=show).pack()

    root.mainloop()

def test9():    # Text组件 Text用于显示和处理多行文本,Text非常灵活和强大,可以用来当作简单的文本编辑器和网页浏览器
    def show(): #    点击显示穹妹图片
        text.image_create(tk.END,image=photo)
        print("添加完成")

    root = tk.Tk()

    text = tk.Text(root, width=300, height=100)
    text.pack()

    #   insert方法可以用于给text组件添加文本
    #   INSERT表示插入到光标位置,END表示插入到最后
    text.insert(tk.INSERT, "I am ZJY")

    #   还可以在text组件中插入image和window组件，此处演示在text中用按钮显示出图片
    photo = tk.PhotoImage(file='img.png')
    text.window_create(tk.INSERT,window=tk.Button(text,text='点我试试',command=show))
    root.mainloop()


"""

Text组件中的三种用法
包括Indexes,Mark,Tag
因内容较多,另写在Text.py中

"""
