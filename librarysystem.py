class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(book, "added to library.")
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully.")
        else:
            print(book, "is not available.")
    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully.")
    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("Available Books:")
            for book in self.books:
                print(book)
library = Library()
library.add_book("Python Basics")
library.add_book("Data Science")
library.add_book("Machine Learning")
library.display_books()
library.issue_book("Python Basics")
library.display_books()
library.return_book("Python Basics")
library.display_books()