import uuid
import datetime as dt

class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = str(uuid.uuid4())
        self.rented_books = {}
    
    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}"
    
    def list_rented_books(self):
        if not self.rented_books:
            print("Not rented books yet.")
            return
        print("List of rented books:")
        for book in self.rented_books.values():
            print(f"Book ID:{book.book_id}, Rented on:{book.rented_at}")

class Book:
    def __init__(self,title,author,year,category,language):
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.language = language
        self.rented_by = None
        self.rented_at = None
        self.return_at = None
        self.is_available = True
        self.is_delete = False

    def __str__(self):
        return f"Title: {self.title}, Book ID: {self.book_id}, Author: {self.author}, Year: {self.year}, Category: {self.category}, Language: {self.language}"

class Library_Manage_Sys:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added.\n {book}, Total books: {len(self.books)}")

    def list_books(self):
        for book in self.books:
            print(book)

    def search_book_by_title(self, title):
        result = []
        print(f"Searching title: {title}")
        found = False
        for book in self.books:
            if title.lower() in book.title.lower() :
                result.append(book)
                print(book)
                found = True
        if not found:
            print(f"No results.")
        return result
        
    def search_book_by_book_id(self, book_id):
        for idx, book in enumerate(self.books):
            if book.book_id == book_id:
                return idx
        return None
    
    def search_book_by_language(self, language):
        result = []
        print(f"Searching language: {language}")
        for book in self.books:
            if book.language.lower() == language.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"No results.")
        return result

    def search_book_by_category(self, category):
        result = []
        print(f"Searching category: {category}")
        for book in self.books:
            if category.lower() in book.category.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"No results.")

    def remove_book_by_book_id(self, book_id):
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return
        self.books[idx].is_delete = True
        print(f"Book removed. {book_id}")

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Member already registered.")
            return
        else:  
            self.members[member.member_id] = member
            print(f"Registration successful. Name: {member.name}, Member ID: {member.member_id}")

    def rent_book_by_book_id(self,book_id, member_id):
        if member_id not in self.members:
            print("Member not registered.")
            return
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return 
        if not self.books[idx].is_available or self.books[idx].is_delete:
            print(f"Book unavailable.{book_id}")
            return
        if len(self.members[member_id].rented_books) >= 2 :
            print("Rental limit reached(max 2 books).")
            return
        self.books[idx].is_available = False
        self.books[idx].rented_by = member_id
        self.books[idx].rented_at = dt.datetime.now().strftime("%Y-%B-%d  %H:%M")
        self.members[member_id].rented_books[book_id] = self.books[idx]
        print(f"Book rented. Book ID: {book_id}  Member ID: {member_id}")

    def check_book_availablility(self,book_id):
        idx = self.search_book_by_book_id(book_id)    
        if idx is None:
            print("Book id not found.")
            return
        if not self.books[idx].is_available or self.books[idx].is_delete:
            print(f"Book unavailable.{book_id}")
            return
        print(f"Book available. {book_id}")

    def return_book(self, book_id):
        idx = self.search_book_by_book_id(book_id)
        if idx is not None:
            self.books[idx].is_available = True
            self.books[idx].return_at = dt.datetime.now().strftime("%Y-%m-%d  %H:%M")
            self.members[self.books[idx].rented_by].rented_books.pop(book_id)
            print(f"Book returned.")
            self.books[idx].rented_by = None
            self.books[idx].rented_at = None
            return
        print("Book id not found!")
    
    def modify_book_details(self,book_id, title=None, author=None, year=None, category=None, language=None):
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return
        if self.books[idx].is_delete:
            print("Cannot modify removed book.")
            return
        if title is not None:
            self.books[idx].title = title
        if author is not None:
            self.books[idx].author = author
        if year is not None:
            self.books[idx].year = year
        if category is not None:
            self.books[idx].category = category
        if language is not None:
            self.books[idx].language = language
            print("Book updated.")

    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            print("Member not found.")
            return
        if name is not None:
            self.members[member_id].name = name
            print("Member updated.")



library = Library_Manage_Sys()

book1 = Book("Python Crash Course", "Eric Matthes", "2015", "Education", "English")
library.add_book(book1)
book2 = Book("Divan Hafez", "Hafez Shirazi", "14th Century", "Poetry", "Persian")
library.add_book(book2)
book3 = Book("One Houndred Years of Solitude", "Gabriel Garcia", "1967", "Fiction", "Spanish")
library.add_book(book3)
book4 = Book("Symphony of the Dead", "Abbas Maroufi", "1989", "Psychological", "Persian")
library.add_book(book4)
print("================================================")

# library.search_book_by_title("on")
# library.search_book_by_language("persian")
# library.search_book_by_category("Education")
print("================================================")

library.remove_book_by_book_id(book1.book_id)
library.check_book_availablility(book1.book_id)

member1 = Member("Nilofar Jafari")
library.register_member(member1)

library.rent_book_by_book_id(book1.book_id, member1.member_id)

print("================================================")

member1.list_rented_books()
# library.check_book_availablility(book2.book_id)

print("================================================")
library.rent_book_by_book_id(book1.book_id, member1.member_id)
library.rent_book_by_book_id(book2.book_id, member1.member_id)
library.rent_book_by_book_id(book3.book_id, member1.member_id)
library.rent_book_by_book_id(book4.book_id, member1.member_id)

member1.list_rented_books()
library.check_book_availablility(book3.book_id)

print("================================================")
library.return_book(book3.book_id)
member1.list_rented_books()
library.check_book_availablility(book3.book_id)

print("=================================================")
library.modify_book_details(book4.book_id, title= "aaaaa")
# library.list_books()

library.update_member(member1.member_id, name="nnnnn")
