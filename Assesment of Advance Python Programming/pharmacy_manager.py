# for Pharmacy Manager:
# 1 Register 
# 2 Login 
# 3 Add Medicine
# 4 View Medicine 
# 5 Delete Medicine
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
class Manager(User):
    def __init__(self,db):
        super().__init__(db)
        self.manager_id = None
# for add manager : 
    def set_manager_id(self,mid):
        self.manager_id = mid
# for add medicine :
    def add_medicine(self):
        size = int(input("enter the no of medicine you want to add = "))
        for _ in range(size):
            name = input("enter the medicine name = ")
            qty = int(input("enter the quntity of medicine = "))
            date = input("enter the qurrent date in (YYYY-MM-DD) formate = ")
            price = float(input("enter the price of medicine = "))
            addby = self.manager_id
            self.detail.cursor.execute("insert into Medicine (Medicine_Name,Qty,Date,Added_By,Price) values (%s,%s,%s,%s,%s)",(name,qty,date,addby,price))
            self.detail.commit()
            print ("Medicine added successfully")
# for view medicine :
    def view (self):
        name = input("enter the name of medicine : ")
        self.detail.cursor.execute("select * from Medicine where Medicine_Name = %s",(name,))
        medicine = self.detail.cursor.fetchall()
        for i in medicine:
            print (f"ID : {i[0]}, Name : {i[1]}, Qty : {i[2]}, Date : {i[3]}, Added By : {i[4]}, Price : {i[5]}")
# for delete medicine :
    def delete (self):
        name = input("enter the name of medicin : ")
        self.detail.cursor.execute("delete from Medicine where Medicine_Name = %s",(name,))
        self.detail.commit()
        if self.detail.cursor.rowcount > 0 :
            print ("Medicine deleted successfully")
        else : 
            print ("Not found")
        