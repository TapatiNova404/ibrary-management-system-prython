import json


def load_books():

    try:

        with open("books.json", "r") as file:

            books = json.load(file)

            return books

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []


def save_books(books):

    with open("books.json", "w") as file:

        json.dump(books, file, indent=4)

def load_admin():

    try:

        with open("admin.json", "r") as file:

            admin = json.load(file)

            return admin

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []