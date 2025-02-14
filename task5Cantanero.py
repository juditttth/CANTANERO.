class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        """Increase the salary by the specified amount."""
        if amount > 0:
            self.salary += amount
            print(f"{self.name}'s salary has been increased by ₱{amount:.2f}. New salary: ₱{self.salary:.2f}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        """Display the details of the employee."""
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary:.2f}")


employee = Employee(name="Irene", position="Software Engineer", salary=60000)


employee.display_employee()
print()  


employee.give_raise(5000)  


employee.display_employee()