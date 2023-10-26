from .cart import Cart
import os
import pickle


class User():

    def __init__(self,username,money):
        self.username = username
        self.money = money
        self.books = []
        self.cart = Cart()
    
    def options(self):
        return [str(method) for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]

    def select_book(self,title,store):
        try:
            book = store.inv_inf[title]
            if store.inventory[book] >0: self.cart.add_book(book)
            else: print("The store doesn't have inventory of "+str(book.title))
        except: print("The store doesn't sell "+str(book.title))


    def buy(self,store):
        if self.cart.total_price < self.money:
            self.money -=  self.cart.total_price
            store.sell(self)
            for book in self.cart.added_books:self.books.append(book)
            self.cart = Cart()
        else: print("Not enough money to buy the selected books")
    
    def ask_catalog(self,store):
        catalog = [b.title for b in store.inventory if store.inventory[b]>0]
        return catalog
    
    def save_changes(self):
        directory_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\Users_data"
        file_path = os.path.join(directory_path, "user_"+self.username+".pkl")
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    def __del__(self):
        self.save_changes()

