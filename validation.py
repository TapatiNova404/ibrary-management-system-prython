def validate_price(price):

    while True:

        try:

            price = float(price)

            if price > 0:

                return price

            else:

                price = input("Enter Valid Price : ")

        except ValueError:

            price = input("Enter Valid Price : ")

def validate_quantity(quantity):

    while True:

        try:

            quantity = int(quantity)

            if quantity >= 0:

                return quantity

            else:

                quantity = input("Enter Valid Quantity : ")

        except ValueError:

            quantity = input("Enter Valid Quantity : ")

def validate_book_id(book_id):

    while True:

        if book_id.strip() == "":

            book_id = input("Enter Valid Book ID : ")

        else:

            return book_id

def validate_name(name):

    while True:

        if name.strip() == "":

            name = input("Enter Valid Name : ")

        else:

            return name