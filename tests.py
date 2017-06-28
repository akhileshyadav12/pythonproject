"""from tkinter import *
mainframe=Tk(className="akhil")
lable=Label(a,text="hello",bg="blue",fg="yellow",relief="raised",cursor="man",height=25,width=50,underline=0)
def fun():
   print(w.get())
   w.delete(0,w.index(10000))

w=Entry(a,bg="blue",bd=3,cursor='heart',fg="black",highlightcolor="cyan",justify="right",relief='sunken',selectbackground=
        'grey',selectborderwidth=7,selectforeground="white")
w.pack()
print(w.get())
but=Button(a,text="click",command=fun)
but.pack()
a.mainloop()"""
from sqlite3 import *


"""top=tkinter.Tk(className="database")
var=tkinter.StringVar()
label=tkinter.Label(top,text=var)
def next():
    var.set("hello")
    label.pack()
btn_next=tkinter.Button(top,text='chut',bg="white",fg="black",cursor="man",height=25,width=50,command=next)
btn_next.pack()
top.mainloop()"""
from tkinter import *
"""db = connect("student.dbf")
cur = db.cursor()
print("select * from user where userName is '{username}' and pass is {passwd}".format(username="akhil",passwd=124))
print(cur.fetchone())"""
from database import *
root = Tk()
root.title("singin")
"""def varification(self):
    data = database()
    if (data.validate(entry_user_name,entry_passwd)):
        print("sing in succussfully")
    else:
        print("unsuccessfull")
label_user_name = Label(root, text="User Name")
entry_user_name = Entry(root)
label_passwd = Label(root, text="Password")
entry_passwd = Entry(root, show="*")

label_user_name.grid(row=1, column=0, sticky=W)
entry_user_name.grid(row=1, column=5)
label_passwd.grid(row=2, column=5, sticky=W)
entry_passwd.grid(row=2, column=5, sticky=W)
btn_singin=Button(root,command=varification)
btn_singin.grid(row=4, column=7)"""
