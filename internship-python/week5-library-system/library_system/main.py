from library_system.library import Library


def print_header():
    print("================================")
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("================================")


def print_menu():
    print("\n1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. View All Members")
    print("8. View Overdue Books")
    print("9. Save & Exit")
    print("0. Exit Without Saving")


def display_books(books, keyword=None):
    if not books:
        print("No books found.")
        return

    if keyword:
        print(f"\nSearch Results for '{keyword}':")
        print("----------------------------------------")

    for index, book in enumerate(books, start=1):
        print(f"{index}. {book.title}")
        print(f"   Author: {book.author}")
        print(f"   ISBN: {book.isbn}")
        print(f"   Year: {book.year if book.year else 'N/A'}")

        if book.available:
            print("   Status: Available\n")
        else:
            print(f"   Status: Borrowed by {book.borrowed_by} (Due: {book.due_date})\n")

    if keyword:
        print(f"Found {len(books)} books matching '{keyword}'")


def display_members(members):
    if not members:
        print("No members found.")
        return

    for index, member in enumerate(members, start=1):
        print(f"{index}. {member.name}")
        print(f"   Member ID: {member.member_id}")
        print(f"   Borrowed Books: {len(member.borrowed_books)}\n")


def main():
    library = Library()
    books_count, members_count = library.load_data()

    print_header()
    print(f"Loaded {books_count} books from file")
    print(f"Loaded {members_count} members from file")

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            year = input("Enter year (optional): ").strip()
            year = int(year) if year.isdigit() else None

            success, message = library.add_book(title, author, isbn, year)
            print(message)

        elif choice == "2":
            name = input("Enter member name: ").strip()
            member_id = input("Enter member ID: ").strip()

            success, message = library.register_member(name, member_id)
            print(message)

        elif choice == "3":
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()

            success, message = library.borrow_book(member_id, isbn)
            print(message)

        elif choice == "4":
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()

            success, message = library.return_book(member_id, isbn)
            print(message)

        elif choice == "5":
            print("\nSearch books by:")
            print("1. Title")
            print("2. Author")
            print("3. ISBN")
            print("4. Show all available books")

            option = input("\nEnter search option: ").strip()

            if option == "1":
                keyword = input("\nEnter title to search: ").strip()
                results = library.search_books("title", keyword)
                display_books(results, keyword)

            elif option == "2":
                keyword = input("\nEnter author to search: ").strip()
                results = library.search_books("author", keyword)
                display_books(results, keyword)

            elif option == "3":
                keyword = input("\nEnter ISBN to search: ").strip()
                results = library.search_books("isbn", keyword)
                display_books(results, keyword)

            elif option == "4":
                results = library.search_books("available")
                display_books(results)

            else:
                print("Invalid search option.")

        elif choice == "6":
            books = library.view_all_books()
            display_books(books)

        elif choice == "7":
            members = library.view_all_members()
            display_members(members)

        elif choice == "8":
            overdue_books = library.view_overdue_books()
            if not overdue_books:
                print("No overdue books.")
            else:
                print("\nOverdue Books:")
                print("----------------------------------------")
                display_books(overdue_books)

        elif choice == "9":
            success, message = library.save_data()
            print(message)
            print("Exiting system...")
            break

        elif choice == "0":
            print("Exiting without saving...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()