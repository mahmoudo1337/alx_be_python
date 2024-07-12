
class Book:
    def __init__(self, title, author, _is_checked_out):
      self.title = title
      self.author = author
      self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False
    def is_available(self):
        return self._is_checked_out
        
    
      
      
class Library:
    def __init__(self):
      self._books = []
    
    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book == title and book.is_available():
                book.check_out()
                self._books.remove(book)
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                self._books.append(book)
    def list_available_books(self):
        return self._books