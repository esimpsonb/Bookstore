

Currently assuming:

    Each costumer has only one cart, and we assume that they will only add things from the same store (edit, it is plausible to asume that we only have one store)

    The books are only aliminated from the inventory when the costumer buys, meaning that maybe there is only one copy of a 
    certain book, but everybody can put it in their cart as long as nobody buys it until that moment.

    change passwords ask 2 times for the username

    prices and quantities are randomaly generated for now

System is the main project right now, users can already save their data, a load method should be implemented and connect it with the login method of the system

users data is being saved with the __del__ method, that is unpredictable sometimes

System.interface doesnt work yet, must fix ASAP

