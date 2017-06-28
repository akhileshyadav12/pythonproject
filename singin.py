from database import *
from tkinter import *
class singin:
    __root=None
    __label_user_name=None
    __label_passwd=None
    __entry_passwd=None
    __entry_user_name=None
    def __varification(self):
        data=database()
        if (data.validate(self.__entry_user_name.get(),int(self.__entry_passwd.get()))):
            print("sing in succussfully")
        else:
            print("unsuccessfull")



    def display(self):
         return self.__root
    def __singin_destroy(self):
        username=self.__entry_user_name.get()
        passwrd=self.__entry_passwd.get()

    def __init__(self):
        self.__root = Tk()
        self. __btn_singin = Button(self.__root, command=self.__varification)
        self.__label_user_name = Label(self.__root, text="User Name")
        self.__entry_user_name = Entry(self.__root)
        self.__label_passwd = Label(self.__root, text="Password")
        self.__entry_passwd = Entry(self.__root, show="*")
        self.__root.title("singin")
        self.__label_user_name.grid(row=1, column=0, sticky=W)
        self.__entry_user_name.grid(row=1,column=5)
        self.__label_passwd.grid(row=2,column=5,sticky=W)
        self.__entry_passwd.grid(row=2, column=5, sticky=W)
        self.__btn_singin.grid(row=4,column=7)

root=singin()
a=root.display()
a.mainloop()
