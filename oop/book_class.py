class Book:
    def __init__(self, title, author, year):
      self.title = str(title)
      self.author = str(author)
      self.year = int(year)
    def __str__(self):
        return f"{self.title} by {self.author}, published in year {self.year}"
    def __del__(self):
        print(f"Deleting {self.title}")
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    
    