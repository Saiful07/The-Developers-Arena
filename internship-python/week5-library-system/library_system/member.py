class Member:
    """Represents a library member"""

    MAX_BORROW_LIMIT = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            return False, "Borrow limit reached (5 books max)"

        if isbn in self.borrowed_books:
            return False, "Book already borrowed by this member"

        self.borrowed_books.append(isbn)
        return True, "Book added to member record"

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            return False, "Book not found in member record"

        self.borrowed_books.remove(isbn)
        return True, "Book removed from member record"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            name=data["name"],
            member_id=data["member_id"]
        )
        member.borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return f"{self.name} ({self.member_id}) - Borrowed: {len(self.borrowed_books)}"