import enum

class ShoppingCart:

    def add(self, itemName, value, itemUnit):
        print('added something ' + itemName)

    def calculatePrice(self):
        return 0

class ItemUnit(enum.IntEnum):
    Item = 0
    Bag = 1
    Gram = 2
    Kilogram = 3