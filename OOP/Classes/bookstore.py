from .order import Order
from .book import Book
import polars as pl
import numpy as np
import os
import pickle

class Bookstore():

    def __init__(self):
        self.name = "Antartica"
        self.orders = []
        self.money = 0
        self.inventory = self.initialize_inventory()
        self.inv_inf = self.books_information()
    
    def initialize_inventory(self):
        df = pl.read_csv(r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\books.csv")
        inv={}
        books_info ={}
        for i in range(len(df)):
            book_info = list(np.array(df[i].select("Title","Author","Genre","ISBN"))[0])
            book_info.append(10000+1000*np.random.randint(10))
            quantity =np.random.randint(10)
            books_info[f"{book_info[0]}"] = Book(book_info)
            inv[books_info[f"{book_info[0]}"]] = quantity

        return inv
    
    def books_information(self):
        information = {}
        for b in self.inventory: information[b.title] = b
        return information

    
    def sell(self,buyer):
        for book in buyer.cart.added_books: self.inventory[book]-=1
        order = Order(buyer)
        self.orders.append(order)
        self.money += self.orders[-1].price
        self.save_changes()
    
    def save_changes(self):
        directory_path = r"C:\Users\enriq\OneDrive\Documents\GitHub\Bookstore\OOP\Data\Bookstore_data"
        file_path = os.path.join(directory_path, self.name+".pkl")
        with open(file_path, "wb") as file:
            pickle.dump(self, file)
