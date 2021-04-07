import unittest
import Supermarket


class ShoppingCartTests(unittest.TestCase):

    # take care of the naming convention of a test - tests start with a leading 'test_'
    def test_buy_apples(self):
        sc = Supermarket.ShoppingCart()
        sc.add('apple', 3, Supermarket.ItemUnit.KILOGRAM)
        self.assertEqual(sc.calculatePrice(), 11.22)

    def test_buy_one_bottle_icedtea(self):
        sc = Supermarket.ShoppingCart()
        sc.add('icedtea', 1, Supermarket.ItemUnit.KILOGRAM)
        self.assertEqual(sc.calculate_price(), 1.04)


if __name__ == '__main__':
    unittest.main()
