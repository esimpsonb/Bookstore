class Cart():

    def __init__(self):
        self.added_books = []
        self.total_price = 0
    
    def add_book(self,book):
        self.added_books.append(book)
        self.total_price += book.price


    def books_in_cart(self):
        print([b.title for b in self.added_books])