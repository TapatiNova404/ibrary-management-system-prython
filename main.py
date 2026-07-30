from operations import *

if admin_login():

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Book Statistics")
        print("9. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            issue_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            book_statistics()

        elif choice == "9":
            print("Thank You")
            break

        else:
            print("Invalid Choice")