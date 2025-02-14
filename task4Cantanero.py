class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")


book1 = Book("The Rain in España", "4reuminct", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Garden of Life", "Ineryss", 1925) 


book1.describe()
print()  
book2.describe()
print()  
book3.describe()