class Order():

    def __init__(self,buyer):
        self.items = buyer.cart.added_books
        self.buyer = buyer
        self.price = sum([b.price for b in self.items])