import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            doj TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    # Delete a Record in DB
    def remove(self, emp_id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (emp_id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, emp_id, name, age, doj, email, gender, contact, address):
        self.cur.execute(
            "UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
            (name, age, doj, email, gender, contact, address, emp_id))
        self.con.commit()

    # Close the connection
    def close(self):
        self.con.close()


def main():
    db = Database("employees.db")

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            doj = input("Enter date of joining (YYYY-MM-DD): ")
            email = input("Enter email: ")
            gender = input("Enter gender: ")
            contact = input("Enter contact number: ")
            address = input("Enter address: ")
            db.insert(name, age, doj, email, gender, contact, address)
            print("Employee added successfully.")

        elif choice == '2':
            employees = db.fetch()
            print("\nEmployees:")
            for emp in employees:
                print(emp)

        elif choice == '3':
            emp_id = int(input("Enter the employee ID to update: "))
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            doj = input("Enter new date of joining (YYYY-MM-DD): ")
            email = input("Enter new email: ")
            gender = input("Enter new gender: ")
            contact = input("Enter new contact number: ")
            address = input("Enter new address: ")
            db.update(emp_id, name, age, doj, email, gender, contact, address)
            print("Employee updated successfully.")

        elif choice == '4':
            emp_id = int(input("Enter the employee ID to delete: "))
            db.remove(emp_id)
            print("Employee deleted successfully.")

        elif choice == '5':
            db.close()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
