class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"And currently studying {self.course}.")  


student1 = Student("Russel Mae", 19, "Education")
student2 = Student("Karla", 20, "Culinary")
student3 = Student("Irene", 20, "Radtech")


student1.introduce()
print()
student2.introduce()
print()
student3.introduce()