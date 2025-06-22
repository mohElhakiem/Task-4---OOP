from Member import Member

class StaffMember(Member):
 def __init__(self,staff_id):
  self.staff_id = staff_id

 def add_book(self):
  print("Add a new book please")