from book import Book
from file_handler import load_books, save_books, load_admin
from validation import (
    validate_book_id,
    validate_name,
    validate_price,
    validate_quantity
)

def admin_login():

    admin = load_admin()

    username = input("Enter Username : ")

    password = input("Enter Password : ")

    for user in admin:

        if user["username"] == username and user["password"] == password:

            print("\nLogin Successful.\n")

            return True

    print("\nInvalid Username or Password.\n")

    return False

def add_book():

    books = load_books()

    book_id = validate_book_id(input("Enter Book ID : "))

    for book in books:

        if book["book_id"] == book_id:

            print("\nBook ID Already Exists.\n")

            return

    title = validate_name(input("Enter Book Title : "))

    author = validate_name(input("Enter Author Name : "))

    category = validate_name(input("Enter Category : "))

    price = validate_price(input("Enter Price : "))

    quantity = validate_quantity(input("Enter Quantity : "))

    new_book = Book(
        book_id,
        title,
        author,
        category,
        price,
        quantity
    )

    books.append(new_book.to_dict())

    save_books(books)

    print("\nBook Added Successfully.\n")

def view_books():

    books = load_books()

    if len(books) == 0:
        print("\nNo Books Available.\n")
        return

    print("\n========== BOOK LIST ==========\n")

    for book in books:

        print(f"Book ID   : {book['book_id']}")
        print(f"Title     : {book['title']}")
        print(f"Author    : {book['author']}")
        print(f"Category  : {book['category']}")
        print(f"Price     : {book['price']}")
        print(f"Quantity  : {book['quantity']}")
        print("-" * 35)

def search_book():

    books = load_books()

    search = input("Enter Book ID or Title : ").lower()

    found = False

    for book in books:

        if (book["book_id"].lower() == search or
                book["title"].lower() == search):

            print("\nBook Found\n")

            print(f"Book ID   : {book['book_id']}")
            print(f"Title     : {book['title']}")
            print(f"Author    : {book['author']}")
            print(f"Category  : {book['category']}")
            print(f"Price     : {book['price']}")
            print(f"Quantity  : {book['quantity']}")

            found = True
            break

    if not found:
        print("\nBook Not Found.\n")

def update_book():

    books = load_books()

    book_id = input("Enter Book ID : ")

    for book in books:

        if book["book_id"] == book_id:

            book["title"] = validate_name(input("Enter New Title : "))

            book["author"] = validate_name(input("Enter New Author : "))

            book["category"] = validate_name(input("Enter New Category : "))

            book["price"] = validate_price(input("Enter New Price : "))

            book["quantity"] = validate_quantity(input("Enter New Quantity : "))

            save_books(books)

            print("\nBook Updated Successfully.\n")

            return

    print("\nBook Not Found.\n")

def delete_book():

    books = load_books()

    book_id = input("Enter Book ID to Delete : ")

    for book in books:

        if book["book_id"] == book_id:

            books.remove(book)

            save_books(books)

            print("\nBook Deleted Successfully.\n")

            return

    print("\nBook Not Found.\n")

def issue_book():

    books = load_books()

    book_id = input("Enter Book ID : ")

    for book in books:

        if book["book_id"] == book_id:

            if book["quantity"] > 0:

                student_name = input("Enter Student Name : ")

                book["quantity"] -= 1

                save_books(books)

                print(f"\nBook Issued Successfully to {student_name}\n")

                return

            else:

                print("\nBook Out of Stock.\n")

                return

    print("\nBook Not Found.\n")

def return_book():

    books = load_books()

    book_id = input("Enter Book ID : ")

    for book in books:

        if book["book_id"] == book_id:

            book["quantity"] += 1

            save_books(books)

            print("\nBook Returned Successfully.\n")

            return

    print("\nBook Not Found.\n")

def book_statistics():

    books = load_books()

    if len(books) == 0:

        print("\nNo Books Available.\n")

        return

    total_books = len(books)

    total_quantity = sum(book["quantity"] for book in books)

    total_value = sum(book["price"] * book["quantity"] for book in books)

    highest_price = max(books, key=lambda x: x["price"])

    lowest_price = min(books, key=lambda x: x["price"])

    print("\n========== LIBRARY STATISTICS ==========\n")

    print(f"Total Book Titles : {total_books}")
    print(f"Total Books Available : {total_quantity}")
    print(f"Total Library Value : ₹{total_value}")

    print("\nMost Expensive Book")
    print(f"{highest_price['title']} - ₹{highest_price['price']}")

    print("\nLeast Expensive Book")
    print(f"{lowest_price['title']} - ₹{lowest_price['price']}")