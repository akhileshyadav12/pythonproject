from sqlite3 import *
class database:
    __db=None
    __cur=None
    def __init__(self):
        self.__db = connect("student.dbf")
        self.__cur = self.__db.cursor()
        try:
            def create_table(self):
                # __query="CREATE TABLE IF NOT EXISTS "+table_name+"()"
                self.__cur.execute("CREATE TABLE IF NOT EXISTS user(userName vchar(50),pass int)")
                self.__db.commit()
                print("within database cunstructor")
        except Exception as e:
            print("create table exceptsion", e)
        create_table(self)
    try:
        def insert_data(self,username,passwd):
            #__inseart_query = "INSERT INTO Student ( " + name + age + school + roll_no + ' )'
            #cur.execute('INSERT INTO Student(Name,Age,School,Roll_No) VALUES({0} {1} {2} {3})'.format(name,age,school,roll_no))
            self.__cur.execute("INSERT INTO user (userName,pass) VALUES ('{name}',{passwd})".format(name=username,passwd=passwd))
            self.__db.commit()
            print("Record created sccessfully")
    except Exception as e:
        print('exception=',e)
    try :
        def validate(self,username,passwd):
            self.__cur.execute("select * from user where userName = %r and pass = %d"%(username,passwd))
            __result=self.__cur.fetchone()
            if(__result[0]==username and __result[1]==passwd):
                return True
            else:
                return False
    except Exception as e:
        print(e)
