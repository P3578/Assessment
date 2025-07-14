import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@rth1995"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists Pharmacy")
mydb.database = "Pharmacy"
sql2 = '''create table if not exists Manager(SR_No int auto_increment primary key,
                                            username varchar(30),
                                            password varchar(30),
                                            Pharmacy_Name varchar(50)
                                            )'''
mycursor.execute(sql2)

sql3 = '''create table if not exists Admin(SR_No int not null auto_increment primary key,
                                            username varchar(30),
                                            password varchar(50)
                                            )'''
mycursor.execute(sql3)

sql = '''create table if not exists Medicine(Id int auto_increment primary key,
                              Medicine_Name varchar(50),
                              Qty int,
                              Date varchar(10),
                              Added_By int,
                              Price decimal(10,2),
                              foreign key (Added_By) references Manager(SR_No)
                              )'''
mycursor.execute(sql)

