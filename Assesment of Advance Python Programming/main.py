from models import Admin, Manager
from db_connection import create_tables

def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. View all Managers")
        print("2. View all Medicines")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            managers = admin.view_all_managers()
            print("\nManagers:")
            for m in managers:
                print(f"ID: {m[0]}, Name: {m[1]}, Pharmacy: {m[2]}")
        elif choice == '2':
            medicines = admin.view_all_medicines()
            print("\nAll Medicines:")
            for m in medicines:
                print(f"ID: {m[0]}, Name: {m[1]}, Qty: {m[2]}, Date: {m[3]}, Added By: {m[4]}, Price: {m[5]}")
        elif choice == '3':
            break
        else:
            print("Invalid option! Try again.")

def manager_menu(manager):
    while True:
        print("\n--- Pharmacy Manager Menu ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Delete Medicine")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                name = input("Medicine name: ")
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                if manager.add_medicine(name, qty, price):
                    print("Medicine added successfully.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            medicines = manager.view_medicines()
            print("\nYour Medicines:")
            for m in medicines:
                print(f"ID: {m[0]}, Name: {m[1]}, Qty: {m[2]}, Date: {m[3]}, Price: {m[5]}")
        elif choice == '3':
            try:
                med_id = int(input("Enter medicine ID to delete: "))
                confirm = input("Are you sure (Y/N)? ").strip().lower()
                if confirm == 'y':
                    if manager.delete_medicine(med_id):
                        print("Medicine deleted.")
                    else:
                        print("Medicine not found or not authorized.")
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            break
        else:
            print("Invalid option! Try again.")

def main():
    create_tables()

    while True:
        print("\n=== Pharmacy Management System ===")
        print("1. Admin Register")
        print("2. Admin Login")
        print("3. Manager Register")
        print("4. Manager Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Admin Name: ")
            password = input("Password: ")
            admin = Admin(name, password)
            if admin.register():
                print("Admin registered successfully.")
        elif choice == '2':
            name = input("Admin Name: ")
            password = input("Password: ")
            admin = Admin(name, password)
            if admin.login():
                print("Login successful.")
                admin_menu(admin)
            else:
                print("Invalid credentials.")
        elif choice == '3':
            name = input("Manager Name: ")
            pharmacy_name = input("Pharmacy Name: ")
            password = input("Password: ")
            manager = Manager(name, password, pharmacy_name)
            if manager.register():
                print("Manager registered successfully.")
        elif choice == '4':
            name = input("Manager Name: ")
            password = input("Password: ")
            manager = Manager(name, password)
            if manager.login():
                print("Login successful.")
                manager_menu(manager)
            else:
                print("Login failed.")
        elif choice == '5':
            print("Thank you for using the system.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
