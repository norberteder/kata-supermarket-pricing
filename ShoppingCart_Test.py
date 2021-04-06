import unittest
import Supermarket

class ShoppingCartTests(unittest.TestCase):

    # take care of the naming convention of a test - tests start with a leading 'test_'
    def test_buyApples(self):
        sc = Supermarket.ShoppingCart()
        sc.add('apple', 3, Supermarket.ItemUnit.Kilogram)
        self.assertEqual(sc.calculatePrice(), 11.22)

    def test_buyOneBottleIcedTea(self):
        sc = Supermarket.ShoppingCart()
        sc.add('icedtea', 1, Supermarket.ItemUnit.Kilogram)
        self.assertEqual(sc.calculatePrice(), 1.04)

if __name__ == '__main__':
    unittest.main()
