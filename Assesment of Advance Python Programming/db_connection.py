import sqlite3

def get_connection():
    return sqlite3.connect("pharmacy.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS managers (
        manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        pharmacy_name TEXT NOT NULL,
        password TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
        med_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        qty INTEGER NOT NULL,
        date_added TEXT NOT NULL,
        added_by INTEGER,
        price REAL NOT NULL,
        FOREIGN KEY (added_by) REFERENCES managers(manager_id)
    )''')

    conn.commit()
    conn.close()
