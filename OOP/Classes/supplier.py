
import polars as pl
    
class Supplier():

    def __init__(self,name):
        self.name = name
        self.supply = self.read_supply()

    def read_supply(self):
        df = pl.read_csv(r"C:\Users\enriq\OneDrive\Documents\GitHub\Bookstore\OOP\Data\Titles.csv")
        titles = df["Title"]
        return {val:10000 for val in titles}

