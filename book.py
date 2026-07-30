class Book:

    def __init__(self, book_id, title, author, category, price, quantity):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self):

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }