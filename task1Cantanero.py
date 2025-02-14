class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


car1 = Car("Ford", "Mustang", 2020)
car2 = Car("BMW", "X5", 2021)

print("car 1 Details:")
car1.display_info()
print("\ncar 2 Details:")  
car2.display_info()