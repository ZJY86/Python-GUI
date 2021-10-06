# @author   :牛子小小说话吊吊
# @time     :2021.10.6
# 本源文件主要记录tkinter事件绑定相关用法

import tkinter as tk

class Event():
    # python tkinter通过bind()方法将函数或者方法绑定到具体事件
    # 当事件被触发时，tkinter会带着事件描述去调用handler()方法

    # 鼠标点击后打印鼠标位置,敲击键盘打印敲击的字母
    @staticmethod
    def t1():
        def callback(event):
            print("鼠标点击位置:x={},y={}".format(event.x, event.y))

        def letter(event):
            print("键盘输入:{}".format(event.char))

        def where(event):
            print("鼠标轨迹:x={},y={}".format(event.x, event.y))

        root = tk.Tk()

        # 直接对窗体绑定事件,<Button-1>代表鼠标左键，callback是反馈
        root.bind("<Button-1>", callback)

        # 只有组件获得焦点的时候才能接收键盘事件，可以用focus_set()获得焦点
        # 或者设置takefocus为True 使用Tab把焦点转移
        root.bind("<Key>", letter)
        root.focus_set()

        # 捕捉鼠标轨迹
        root.bind("<Motion>", where)

        tk.mainloop()

if __name__ == '__main__':
    Event.t1()
