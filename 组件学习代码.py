# @author   :牛子小小说话吊吊
# @time     :2021.10.6
# 本源文件主要记录tkinter基本组件的用法

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


    photo = tk.PhotoImage(file='../PyGame/img.png')
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
    photo = tk.PhotoImage(file='../PyGame/img.png')
    text.window_create(tk.INSERT,window=tk.Button(text,text='点我试试',command=show))
    root.mainloop()
    """

        Text组件中的三种用法
        包括Indexes,Mark,Tag  
        因内容较多,另写在Text.py中

    """

class Canvas:
    @staticmethod
    def t1():# canvas初体验
        root = tk.Tk()

        canvas = tk.Canvas(root, width=200, height= 100)
        canvas.pack()

        # 可以在canvas对象中画线 画矩阵 插入文本 椭圆/圆
        l1 = canvas.create_line(0, 50, 200, 50, fill="yellow")
        l2 = canvas.create_line(100, 0, 100, 100, fill="blue")
        r1 = canvas.create_rectangle(50, 25, 150, 75, fill="yellow")
        o1 = canvas.create_oval(40, 20, 120, 100, fill="pink")
        t1 = canvas.create_text(100, 50, text='zjy is your father', fill="black")

        #   可以用某些方法修改Canvas中的对象
        canvas.coords(l1, 0, 25, 200, 25)
        canvas.itemconfig(r1, fill="red")
        canvas.delete(l2)

        root.mainloop()

    @staticmethod
    def t2(): # canvas绘制多边形
        root = tk.Tk()

        root.mainloop()

    @staticmethod
    def t3(): # 利用canvas写一个简单的画图程序
        def piant(event):
            d = 0.001
            x1, y1 = (event.x - d), (event.y - d)
            x2, y2 = (event.x + d), (event.y + d)
            canvas.create_oval(x1, y1, x2, y2, fill="black")

        root = tk.Tk()

        canvas = tk.Canvas(root, width=400, height=200)
        canvas.pack()

        canvas.bind("<B1-Motion>", piant)

        tk.Button(root, text='清空全部', command=(lambda x=tk.ALL: canvas.delete(x))).pack()

        root.mainloop()

class Menu:
    '''
        菜单功能，不建议用按钮或其他组件实现菜单功能
        tk.Menu()可以创建一个顶级菜单，然后往顶级菜单里添加组件
    '''
    @staticmethod
    def t1(): # 简单的菜单实现
        def callback():
            print('已调用')

        root = tk.Tk()

        menubar = tk.Menu(root)
        menubar.add_command(label='Hello', command=callback)
        menubar.add_command(label='Quit', command=root.quit)

        # 再root中配置菜单
        root.config(menu=menubar)

        root.mainloop()

    @staticmethod
    def t2(): # 下拉菜单的实现
        def callback():
            print('被调用了')

        root = tk.Tk()

        menubar = tk.Menu(root)     # 顶层菜单
        filemenu = tk.Menu(menubar, tearoff=False)  # 下拉菜单

        lst1 = ['打开', '保存', '退出']
        for i in lst1:
            filemenu.add_command(label=i, command=callback)
            filemenu.add_separator()

        #   用add_cascade方法把下拉菜单和顶层菜单进行绑定
        menubar.add_cascade(label='文件', menu=filemenu)


        root.config(menu=menubar)
        root.mainloop()

    @staticmethod
    def t3():   # 弹出菜单
        def callback():
            print("已调用")

        root = tk.Tk()
        frame = tk.Frame(root, width=512, height=512)
        frame.pack()

        menu = tk.Menu(frame, tearoff=False)
        menu.add_command(label='好家伙', command=callback)
        menu.add_command(label='GG', command=callback)


        def popup(event):    # 弹出菜单
            menu.post(event.x, event.y)

        frame.bind("<Button-3>", popup)

        root.mainloop()

    # 菜单还能增加单选或者多选按钮
    @staticmethod
    def t4():
        def callback():
            print('于menu.t4()中被调用了')

        root = tk.Tk()

        # 顶级菜单
        menubar = tk.Menu(root)

        # checkbutton关联变量
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        v3 = tk.IntVar()

        # 下拉菜单
        filemenu = tk.Menu(menubar,tearoff=True)            # 把单选按钮和IntVar绑定 被选了就是1 没选就是0
        filemenu.add_checkbutton(label='菜单单选1', command=callback, variable=v1)
        filemenu.add_checkbutton(label='菜单单选2', command=callback, variable=v2)
        filemenu.add_separator()
        filemenu.add_checkbutton(label='菜单单选3', command=callback, variable=v3)

        # 把下拉菜单加到顶级菜单中
        menubar.add_cascade(label='下拉菜单', menu=filemenu)

        # 复选按钮关联变量
        v = tk.IntVar()
        v.set(1)
        editmenu = tk.Menu(menubar, tearoff=True)
        # 添加复选按钮                                             # value表示复选被选中后绑定Var变量的值
        editmenu.add_radiobutton(label='菜单复选1', command=callback, variable=v, value=1)
        editmenu.add_radiobutton(label='菜单复选2', command=callback, variable=v, value=2)
        editmenu.add_separator()
        editmenu.add_radiobutton(label='菜单复选3', command=callback, variable=v, value=3)

        # 把菜单添加到顶级菜单中
        menubar.add_cascade(label='复选按钮', menu=editmenu)

        # 配置菜单
        root.config(menu=menubar)
        root.mainloop()


class Menubutton:
    # 菜单按钮
    # 可以出现在窗口任意位置的弹出下拉菜单

    @staticmethod
    def t1():
        def callback():
            print('被调用了')

        root = tk.Tk()

        menubutton = tk.Menubutton(root, text='这是个MenuButton', relief=tk.RAISED)
        menubutton.pack()

        # 下拉菜单和Menubutton绑定
        filemenu = tk.Menu(menubutton, tearoff=True)
        filemenu.add_command(label='按钮1', command=callback)
        filemenu.add_separator()
        filemenu.add_checkbutton(label='单选1', command=callback, selectcolor='yellow')
        filemenu.add_separator()
        filemenu.add_command(label='退出按钮', command=root.quit)
        # 配置菜单

        menubutton.config(menu=filemenu)

        root.mainloop()

class OptionMenu:
    # 选项菜单,可以把listbox加入其中
    # 只需要一个StringVar变量就可以记录用户的选择
    @staticmethod
    def t1():
        def callback():
            print("选项菜单的当前值为{}".format(strvar.get()))

        options=['zsj', 'zjy', 'tjj', 'haohao', 'rcx', 'ljj', 'weber']

        root = tk.Tk()

        strvar = tk.StringVar()
        # 选项菜单显示的初始值
        strvar.set(options[0])

        # 直接按位置传入参数
        tk.OptionMenu(root, strvar, *options).pack()

        # 按钮绑定函数，输出当前值
        tk.Button(root, text='获取选项菜单当前值', command=callback).pack()

        root.mainloop()


class Message:
    # label的变体，可以显示多行文本消息
    # 可以自动换行，并调整文本的尺寸使其适应给定的尺寸
    @staticmethod
    def t1():
        root = tk.Tk()

        tk.Message(root, text='嘉然，我真的好喜欢你呀，为了你我要电牛子！！！！！！！！！！', width=75).pack()

        root.mainloop()

class Spinbox():

    # Spinbox是Entry组件的变体，用法相似，用于从固定的值中选一个输入
    # Spinbox可以通过元组或者范围来指定用户输入的内容
    @staticmethod
    def t1():
        root = tk.Tk()

        # 通过范围指定内容
        # spinbox= tk.Spinbox(root, from_=0, to=10)

        # 通过元组指定范围
        values = ('a', 'b', 'c', 'd', 'e')
        tk.Spinbox(root, values=values).pack()

        root.mainloop()

class PanedWindow():

    # 是一个空间管理组件，为组件提供一个框架，允许让用户调整应用程序的空间划分

    # 创建一个三窗格的PanedWindow(嵌套PanerWindow结构)
    @staticmethod
    def t1():
        # showhandle显示一个移动手柄，sashrelief显示划分线
        pw1 = tk.PanedWindow(showhandle = True, sashrelief = tk.SUNKEN)
        pw1.pack(fill=tk.BOTH, expand=1)

        left = tk.Label(pw1, text='左')
        pw1.add(left)

        # 嵌套
        pw2 = tk.PanedWindow(orient=tk.VERTICAL,showhandle = True)
        top = tk.Label(pw2, text='顶')
        pw2.add(top)

        bottom = tk.Label(pw2, text='底')
        pw2.add(bottom)

        pw1.add(pw2)
        tk.mainloop()


class Toplevel():
    # Toplevel类似于Frame，但是其是一个独立的顶级窗口，通常有标题栏、边框等
    # 通常用于显示额外的窗口、对话框和其他弹出窗口中

    # 单击按钮创建新窗口
    @staticmethod
    def t1():
        def create():
            toplevel = tk.Toplevel()
            toplevel.title('新弹出chuangkou')

            tk.Message(toplevel, text='还要多远才能进入你的心').pack()

        root = tk.Tk()

        tk.Button(root, text='单击创建新窗口', command=create).pack()

        root.mainloop()

    # tkinter提供一系列方法与窗口管理器进行交互
    # attributes()方法可以设置或获取窗口属性

#################
# tkinter组件基础部分到此结束，事件绑定部分在PythonEvent.py之中
################

if __name__ == '__main__':
    Toplevel.t1()
