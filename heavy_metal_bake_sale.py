import unittest


class BakeSale:
    def __init__(self):
        self.brownieQuantity = 48
        self.browniePrice = 0.65
        self.muffinQuantity = 36
        self.muffinPrice = 1.0
        self.cakePopQuantity = 24
        self.cakePopPrice = 1.35
        self.waterQuantity = 30
        self.waterPrice = 1.50

    def get_brownie_quantity(self) -> int:
        return self.brownieQuantity

    def get_water_quantity(self):
        return self.waterQuantity

    def get_cake_pop_quantity(self):
        return self.cakePopQuantity

    def get_muffin_quantity(self):
        return self.muffinQuantity


class MyTestCase(unittest.TestCase):
    def test_saleStartsWithProperItemsQuantity(self):
        self.sale = BakeSale()

        self.assertEqual(self.sale.get_brownie_quantity(), 48)
        self.assertEqual(self.sale.get_muffin_quantity(), 36)
        self.assertEqual(self.sale.get_cake_pop_quantity(), 24)
        self.assertEqual(self.sale.get_water_quantity(), 30)


if __name__ == '__main__':
    unittest.main()
