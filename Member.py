class Member:
 def __init__(self,name,membership_id,borrowed_books):
  self.name = name
  self.__membership_id = membership_id
  self.borrowed_books = borrowed_books

 def get_id(self):
  return self.__membership_id

 def borrow_book(self):
  if self.borrowed_books == "The Rabbit" :
   print("This book is available")
  else :
   print("not found")

 def return_book(self):
  if self.borrowed_books == "The Rabbit":
   print("Please return the book")
  else :
   print("you didn't take any book from us yet")