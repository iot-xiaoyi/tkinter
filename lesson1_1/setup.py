#coding:utf-8
from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog as dialog

def btn_msg_box_cb():
    msg.showinfo(title='提示', message="This is a messagebox")

root = Tk()
root.geometry('420x100')
root.resizable(0, 0)
root.title('tkinter V1.0')

label_edit = Label(root,  text='编辑框:',  font=("", 12), width=15, height=2)
label_edit.grid(row=0, sticky=W)
text_edit = Text(root, width=40, height=2)
text_edit.grid(row=0, column=1, columnspan=2, sticky=W)

label_msg_box = Label(root,  text='消息框:', font=("", 12), width=15, height=2)
label_msg_box.grid(row=1, sticky=W)

btn_msg_box = Button(root, text='打开',  width=8, height=1, padx=10, command=btn_msg_box_cb)
btn_msg_box.grid(row=1, column=1, sticky=W)

root.mainloop()