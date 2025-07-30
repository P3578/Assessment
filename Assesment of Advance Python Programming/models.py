from datetime import datetime
from db_connection import get_connection

class BaseUser:
    def __init__(self, name, password):
        self.name = name.strip()
        self.password = password.strip()

    def validate_login(self, table):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE name = ? AND password = ?", (self.name, self.password))
        result = cursor.fetchone()
        conn.close()
        return result

class Admin(BaseUser):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.admin_id = None

    def register(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO admins (name, password) VALUES (?, ?)", (self.name, self.password))
        conn.commit()
        conn.close()
        return True

    def login(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE name = ? AND password = ?", (self.name, self.password))
        result = cursor.fetchone()
        conn.close()
        if result:
            self.admin_id = result[0]
            return True
        return False

    def view_all_managers(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT manager_id, name, pharmacy_name FROM managers")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def view_all_medicines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicines")
        rows = cursor.fetchall()
        conn.close()
        return rows


class Manager(BaseUser):
    def __init__(self, name, password, pharmacy_name=None):
        super().__init__(name, password)
        self.pharmacy_name = pharmacy_name
        self.manager_id = None

    def register(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO managers (name, pharmacy_name, password) VALUES (?, ?, ?)",
                       (self.name, self.pharmacy_name, self.password))
        conn.commit()
        conn.close()
        return True

    def login(self):
        user = self.validate_login("managers")
        if user:
            self.manager_id = user[0]
            return True
        return False

    def add_medicine(self, name, qty, price):
        if not name or qty <= 0 or price <= 0:
            raise ValueError("Invalid data provided.")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medicines (name, qty, date_added, added_by, price) VALUES (?, ?, ?, ?, ?)",
                       (name, qty, datetime.now().strftime("%Y-%m-%d"), self.manager_id, price))
        conn.commit()
        conn.close()
        return True

    def view_medicines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicines WHERE added_by = ?", (self.manager_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_medicine(self, med_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicines WHERE med_id = ? AND added_by = ?", (med_id, self.manager_id))
        if cursor.fetchone():
            cursor.execute("DELETE FROM medicines WHERE med_id = ?", (med_id,))
            conn.commit()
            conn.close()
            return True
        conn.close()
        return False
