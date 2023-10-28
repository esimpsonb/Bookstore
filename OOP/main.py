
from Classes.system import System
from Classes.book import Book
from Classes.user import User
from Classes.bookstore import Bookstore
from Classes.cart import Cart
from Classes.supplier import Supplier
from Classes.delivery import Delivery_Boy

Enrique = User("esimpson",10000000)
Antartica = Bookstore()
Fabrica = Supplier("Fabrica")
for book in Antartica.inventory:
    libreke = book
    break 

address1 = "228 Republica, Viña del Mar, Chile"
address2 = "130 Ecuador, Viña del Mar, Chile"


Antartica.buy(libreke,1,Fabrica)

Benjamin = Delivery_Boy()
print(Benjamin.distance_matrix([address1,address2]))

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


