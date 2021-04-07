import enum


class ShoppingCart:

    def add(self, item_name, value, item_unit):
        print('added something ' + item_name)

    def calculate_price(self):
        return 0


class ItemUnit(enum.IntEnum):
    ITEM = 0
    BAG = 1
    GRAM = 2
    KILOGRAM = 3
