
from Classes.system import System
from Classes.book import Book
from Classes.user import User
from Classes.bookstore import Bookstore
from Classes.cart import Cart
from Classes.supplier import Supplier


Enrique = User("esimpson",10000000)
Antartica = Bookstore()
Fabrica = Supplier("Fabrica")
for book in Antartica.inventory:
    libreke = book
    break 

Antartica.buy(libreke,1,Fabrica)


#print(Enrique.options())


#sistema = System(Antartica)

#sistema.interface(Enrique,Antartica)
#Enrique.save_changes()

#print(Antartica.inventory)

#print(Antartica.inv_inf)

#print(Enrique.ask_catalog(Antartica))

#Enrique.select_book('Ayn Rand Answers',Antartica)
#Enrique.select_book(Biblia,Antartica)

#Enrique.buy(Antartica)

#print([book.title for book in Enrique.books])
#print(Enrique.money)
#print(Antartica.money)
#print(Antartica.orders[-1].items)


