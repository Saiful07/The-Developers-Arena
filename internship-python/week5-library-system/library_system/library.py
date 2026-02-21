import json
import os
from datetime import datetime
from library_system.book import Book
from library_system.member import Member


class Library:
    """Main controller for the Library Management System"""

    def __init__(self):
        self.books = {}      # {isbn: Book}
        self.members = {}    # {member_id: Member}
        self.books_file = self._get_books_file_path()
        self.members_file = self._get_members_file_path()

    # ----------------------------
    # FILE PATH HANDLING
    # ----------------------------

    def _get_books_file_path(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(base_dir, "data", "books.json")

    def _get_members_file_path(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(base_dir, "data", "members.json")

    # ----------------------------
    # BOOK MANAGEMENT
    # ----------------------------

    def add_book(self, title, author, isbn, year=None):
        if isbn in self.books:
            return False, "Book with this ISBN already exists"

        book = Book(title, author, isbn, year)
        self.books[isbn] = book
        return True, "Book added successfully"

    def remove_book(self, isbn):
        if isbn not in self.books:
            return False, "Book not found"

        del self.books[isbn]
        return True, "Book removed successfully"

    def find_book_by_isbn(self, isbn):
        return self.books.get(isbn)

    def search_books(self, search_type, keyword=None):
        results = []

        for book in self.books.values():
            if search_type == "title" and keyword.lower() in book.title.lower():
                results.append(book)

            elif search_type == "author" and keyword.lower() in book.author.lower():
                results.append(book)

            elif search_type == "isbn" and keyword == book.isbn:
                results.append(book)

            elif search_type == "available" and book.available:
                results.append(book)

        return results

    def view_all_books(self):
        return list(self.books.values())

    def view_overdue_books(self):
        overdue = []
        for book in self.books.values():
            if not book.available and book.is_overdue():
                overdue.append(book)
        return overdue

    # ----------------------------
    # MEMBER MANAGEMENT
    # ----------------------------

    def register_member(self, name, member_id):
        if member_id in self.members:
            return False, "Member ID already exists"

        member = Member(name, member_id)
        self.members[member_id] = member
        return True, "Member registered successfully"

    def find_member(self, member_id):
        return self.members.get(member_id)

    def view_all_members(self):
        return list(self.members.values())

    # ----------------------------
    # BORROW / RETURN
    # ----------------------------

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        if not book.available:
            return False, "Book is already borrowed"

        success, message = member.borrow_book(isbn)
        if not success:
            return False, message

        book.check_out(member_id)
        return True, "Book borrowed successfully"

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = member.return_book(isbn)
        if not success:
            return False, message

        was_overdue = book.is_overdue()
        overdue_days = book.days_overdue()
        book.return_book()

        if was_overdue:
            fine = overdue_days * 10
            return True, f"Book returned. Overdue by {overdue_days} days. Fine: ₹{fine}"

        return True, "Book returned successfully"

    # ----------------------------
    # DATA PERSISTENCE
    # ----------------------------

    def load_data(self):
        books_loaded = 0
        members_loaded = 0

        # Load Books
        try:
            with open(self.books_file, "r") as f:
                books_data = json.load(f)
                for book_dict in books_data:
                    book = Book.from_dict(book_dict)
                    self.books[book.isbn] = book
                books_loaded = len(self.books)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = {}

        # Load Members
        try:
            with open(self.members_file, "r") as f:
                members_data = json.load(f)
                for member_dict in members_data:
                    member = Member.from_dict(member_dict)
                    self.members[member.member_id] = member
                members_loaded = len(self.members)
        except (FileNotFoundError, json.JSONDecodeError):
            self.members = {}

        return books_loaded, members_loaded

    def save_data(self):
        try:
            with open(self.books_file, "w") as f:
                json.dump([book.to_dict() for book in self.books.values()], f, indent=4)

            with open(self.members_file, "w") as f:
                json.dump([member.to_dict() for member in self.members.values()], f, indent=4)

            return True, "Data saved successfully"

        except Exception as e:
            return False, f"Error saving data: {e}"

    def backup_data(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        backup_dir = os.path.join(base_dir, "data", "backup")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        try:
            os.makedirs(backup_dir, exist_ok=True)

            books_backup = os.path.join(backup_dir, f"books_backup_{timestamp}.json")
            members_backup = os.path.join(backup_dir, f"members_backup_{timestamp}.json")

            with open(books_backup, "w") as f:
                json.dump([book.to_dict() for book in self.books.values()], f, indent=4)

            with open(members_backup, "w") as f:
                json.dump([member.to_dict() for member in self.members.values()], f, indent=4)

            return True, "Backup created successfully"

        except Exception as e:
            return False, f"Backup failed: {e}"

    # ----------------------------
    # STATISTICS
    # ----------------------------

    def get_statistics(self):
        total_books = len(self.books)
        available_books = sum(1 for book in self.books.values() if book.available)
        borrowed_books = total_books - available_books
        total_members = len(self.members)

        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": total_members
        }