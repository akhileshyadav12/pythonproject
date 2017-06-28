from tkinter import *
a=Tk()
v=IntVar()
l=Label(a)
l.pack()
def fun():
    if v.get()==1:
        l.config(text="radio1 clicked")
    if v.get()==2:
        l.config(text="radio2 clicked")
r=Radiobutton(a,text="radio button1",value=1,variable=v,command=fun)
r1=Radiobutton(a,text="radio button2",value=2,variable=v,command=fun)
r.pack()
r1.pack()
a.mainloop()
