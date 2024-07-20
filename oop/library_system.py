class Book:
    def __init__(self, title, author):
      self.title = title
      self.author = author
      
      
      
class EBook(Book):
    def __init__(self, file_size):
      self.file_size = file_size

class PrintBook(Book):
    def __init__(self, name, page_count):
      self.page_count = page_count

## __str__
## super().__init__
class Library:
    def __init__(self, books):
      self.books = []
      
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)