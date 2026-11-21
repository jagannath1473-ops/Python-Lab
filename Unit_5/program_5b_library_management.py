class Library:
    def __init__(self):
        self.books = ["Python", "AI Basics", "Data Science"]

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print("-", book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book not available")


library = Library()
library.display_books()
requested_book = input("Enter book to issue: ")
library.issue_book(requested_book)
