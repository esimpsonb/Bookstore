

Currently assuming:

    Each costumer has only one cart, and we assume that they will only add things from the same store (edit, it is plausible to asume that we only have one store)

    The books are only aliminated from the inventory when the costumer buys, meaning that maybe there is only one copy of a 
    certain book, but everybody can put it in their cart as long as nobody buys it until that moment.

    change passwords ask 2 times for the username

    prices and quantities are randomaly generated for now

users data is being saved with the __del__ method, that is sometimes unpredictable

The matrix distance is not accurate (paid APIs would fix this)
