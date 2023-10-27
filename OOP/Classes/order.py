import os
import pickle

class Order():

    def __init__(self,buyer):
        self.items = buyer.cart.added_books
        self.buyer = buyer
        self.price = sum([b.price for b in self.items])
        self.save_changes()

    def save_changes(self):
        directory_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\Orders_data"
        file_count = len(os.listdir(directory_path))
        file_path = os.path.join(directory_path, "Order_"+str(file_count)+".pkl")
        with open(file_path, "wb") as file:
            pickle.dump(self, file)
