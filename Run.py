from Book import Book
from Member import Member
from StaffMember import StaffMember

book1 = Book("The Tunnel","Sharlock Holmes","544",True)
member1 = Member("Tom","1899","The Rabbit")
staff1 = StaffMember("667")

print(book1.display_info())


print(member1.name,member1.get_id(),member1.borrowed_books)

member1.borrow_book()

member1.return_book()

print(staff1.staff_id)

staff1.add_book()

