import json


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def to_dict(self):
        return {"name": self.name, "age": self.age, "salary": self.salary}

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeesManager:
    FILE_PATH = "employees.json"

    def __init__(self):
        self.employees = self.load_from_file()

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_to_file()

    def list_employees(self):
        return self.employees

    def remove_by_age_range(self, min_age, max_age):
        self.employees = [e for e in self.employees if not (min_age <= e.age <= max_age)]
        self.save_to_file()

    def find_employee(self, name):
        return next((e for e in self.employees if e.name == name), None)

    def update_salary(self, name, new_salary):
        employee = self.find_employee(name)
        if employee:
            employee.salary = new_salary
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open(self.FILE_PATH, "w") as f:
            json.dump([e.to_dict() for e in self.employees], f)

    def load_from_file(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                return [Employee(**data) for data in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username == "admin" and password == "admin"

    def run(self):
        if not self.login():
            print("Invalid login credentials.")
            return

        while True:
            print("\n1. Add Employee")
            print("2. List Employees")
            print("3. Remove Employees by Age Range")
            print("4. Update Employee Salary")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
                self.manager.add_employee(Employee(name, age, salary))
                print("Employee added.")
            elif choice == "2":
                for emp in self.manager.list_employees():
                    print(emp)
            elif choice == "3":
                min_age = int(input("Enter min age: "))
                max_age = int(input("Enter max age: "))
                self.manager.remove_by_age_range(min_age, max_age)
                print("Employees removed.")
            elif choice == "4":
                name = input("Enter employee name: ")
                new_salary = float(input("Enter new salary: "))
                if self.manager.update_salary(name, new_salary):
                    print("Salary updated.")
                else:
                    print("Employee not found.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    FrontendManager().run()
