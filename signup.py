from  tkinter import  *
from database import *
def singup():
    singup_frame=Tk()
    singup_frame.title("singup")

    label_user_name=Label(singup_frame,text="User Name")
    label_user_name.grid(row=1,column=0,sticky=W)
    entry_user_name=Entry(singup_frame)
    entry_user_name.grid(row=1,column=5,sticky=W)
    text_passwd=Label(singup_frame,text="New Password")
    text_passwd.grid(row=2,column=0,sticky=W)
    entry_passwd=Entry(singup_frame)
    entry_passwd.grid(row=2,column=5)
    text_repasswd=Label(singup_frame,text="Conform Password")
    text_repasswd.grid(row=3,column=0)
    entry_repasswd=Entry(singup_frame)
    entry_repasswd.grid(row=3,column=5)


    def singupdestroy():

        if entry_passwd.get()==entry_repasswd.get():
            data = database()
            data.insert_data(entry_user_name.get(),entry_passwd.get())
            singup_frame.destroy()
            singup_message()
        else:
            singup_frame.destroy()
            singup()
    btn_singup=Button(singup_frame,text="singup",command=singupdestroy)
    btn_singup.grid(row=5,column=7)
    singup_frame.mainloop()

def singup_message():

    singup_success_frame=Tk()
    lable=Label(singup_success_frame,text="singup succesfully")
    lable.pack()
    #singup_frame.destroy()
    singup_success_frame.mainloop()
singup()