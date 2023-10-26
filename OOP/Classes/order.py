import os


class Order():

    def __init__(self,buyer):
        self.items = buyer.cart.added_books
        self.buyer = buyer
        self.price = sum([b.price for b in self.items])

    def save_changes(self):
        directory_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\Orders_data"
        file_count = len(os.listdir(folder_path))
        file_path = os.path.join(directory_path, "user_"+buyer.username+str(file_count)+".pkl")
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    def __del__(self):
        self.save_changes()