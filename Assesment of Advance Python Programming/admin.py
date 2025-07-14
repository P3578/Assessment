# for Admin :
# 1 Register
# 2 Login
# 3 View all manager
# 4 View all medicine
import mysql
import mysql.connector
from getpass import getpass
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@rth1995",
        database = "Pharmacy"
        )
        self.cursor = self.mydb.cursor()
    def commit(self):
        self.mydb.commit()
    def close(self):
        self.mydb.close()
# for Register :
class User :
    def __init__(self,detail):
        self.detail = detail
    def register (self,table):
        username = input ("enter the name : ")
        password = getpass ("enter the password : ")
        try : 
            self.detail.cursor.execute(f"insert into {table} (username,password) values(%s ,%s)",(username,password))
            self.detail.commit()
            print ("Register successfully")
        except mysql.connector.IntegrityError:
            print ("Username already exists")
# For Login :
    def login(self,table):
        name = input("enter the name : ")
        password = getpass("enter the password : ")
        self.detail.cursor.execute(f"select * from {table} where username = %s and password = %s",(name,password))
        user = self.detail.cursor.fetchone()
        return user
class Admin(User):
    def __init__(self,detail):
        super().__init__(detail)

# view all manager :
    def viewmanager(self):
        self.detail.cursor.execute("select * from Manager")
        manager = self.detail.cursor.fetchall()
        for i in manager:
            print (f"ID : {i[0]} , Username : {i[1]}")
# view all medicine :
    def viewmedicine(self):
        self.detail.cursor.execute("select * from Medicine")
        medicine = self.detail.cursor.fetchall()
        for i in medicine:
            print (f"ID : {i[0]}, Name : {i[1]}, Qty : {i[2]}, Price : {i[3]}, Added By : {i[4]}")
        
        

    