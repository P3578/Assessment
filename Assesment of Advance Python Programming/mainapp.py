#from module import admin,pharmacy_manager
from admin import *
from pharmacy_manager import *
class PharmacyApp:
    def __init__(self):
        self.mydb = Database()
        self.admin = Admin(self.mydb)
        self.manager = Manager(self.mydb)

# for admin : 
    def admin_menu(self):
        while True:
            print ("\n--- Admin Menu ---")
            print ("1. View all manager")
            print ("2. View all medicine")
            print ("3. Exit")
            choice = input ("enter the choice : ")
            match choice:
                case "1" :
                    self.admin.viewmanager()
                case "2" :
                    self.admin.viewmedicine()
                case "3" :
                    break

# for manager :
    def manager_menu(self):
        while True:
            print ("\n--- Manager Menu ---")
            print ("1. Add Medicine")
            print ("2. View Medicine")
            print ("3. Delete Medicine")
            print ("4. Exit")
            choice = input ("enter the choice : ")
            match choice:
                case "1" :
                    self.manager.add_medicine()
                case "2" :
                    self.manager.view()
                case "3" :
                    self.manager.delete()
                case "4" :
                    break

# for register :
    def main_menu(self):
        while True:
            print ("\n ------------ Wel-Come to Pharmacy Management System ------------")
            print ("1. Admin Register")
            print ("2. Admin Login")
            print ("3. Manager Register")
            print ("4. Manager Login")
            print ("5. Exit")
            choice = input ("enter the choice : ")
            match choice:
                case "1" :
                    self.admin.register("Admin")
                case "2" :
                    user = self.admin.login("Admin")
                    if user :
                        print ("Admin loggedin")
                        self.admin_menu()
                    else :
                        print ("Admin not exists")
                case "3" :
                    self.manager.register("Manager")
                case "4" :
                    user = self.manager.login("Manager")
                    if user:
                        print ("Manager loggedin")
                        self.manager.set_manager_id(user[0]) 
                        self.manager_menu()
                    else :
                        print ("Manager not exists")
                case "5" :
                    break
# for run programm:
if __name__ == "__main__" :
    app = PharmacyApp()
    app.main_menu()