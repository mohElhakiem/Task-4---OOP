class Book:
 def __init__(self,title,author,isbn,is_available):
  self.title = title
  self.author = author
  self.__isbn = isbn
  self.is_available = is_available

 def get_isbn(self):
  return self.__isbn

 def display_info(self):
  print(self.title)
  print(self.author)
  print(self.get_isbn())
  print(self.is_available)
