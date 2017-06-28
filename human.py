from database import *
class Human:
    __name=""
    __age=0
    def __init__(self,name,age,school,roll_no):
        create_table()
        insert_data(name,age,school,roll_no)
        self.__name=name
        self.__age=age
    @property

    def __repr__(self):
        return "Hello I am {name} and my age is {age}".format(name=self.__name,age=self.__age)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __str__(self):
       return "Hello I am {name} and my age is {age}".format(name=self.__name,age=self.__age)
a=Human('akhilesh yadav',20,'skbvm',1)