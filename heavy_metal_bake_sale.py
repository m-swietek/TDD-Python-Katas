import unittest
from unittest.mock import MagicMock

class BakeSale:
    def __init__(self, brownies: int, muffins: int, cake_pops: int, waters: int):
        self.browniePrice = 0.65
        self.muffinPrice = 1.0
        self.cakePopPrice = 1.35
        self.waterPrice = 1.50
        self.brownieQuantity = brownies
        self.muffinQuantity = muffins
        self.cakePopQuantity = cake_pops
        self.waterQuantity = waters

    def get_brownie_quantity(self) -> int:
        return self.brownieQuantity

    def get_water_quantity(self):
        return self.waterQuantity

    def get_cake_pop_quantity(self):
        return self.cakePopQuantity

    def get_muffin_quantity(self):
        return self.muffinQuantity

    def sell_brownie(self, quantity: int):
        if quantity > self.brownieQuantity:
            self.not_enough_items_warning()
        else:
            self.brownieQuantity -= 1

    def sell_muffin(self, quantity: int):
        self.muffinQuantity -= 1

    def sell_cake_pop(self, quantity: int):
        self.cakePopQuantity -= 1

    def sell_water(self, quantity: int):
        self.waterQuantity -= 1

    def not_enough_items_warning(self):
        print("Not enough stock")


class MyTestCase(unittest.TestCase):

    def test_saleStartsWithProperItemsQuantity(self):
        self.sale = BakeSale(48, 36, 24, 30)
        self.assertEqual(self.sale.get_brownie_quantity(), 48)
        self.assertEqual(self.sale.get_muffin_quantity(), 36)
        self.assertEqual(self.sale.get_cake_pop_quantity(), 24)
        self.assertEqual(self.sale.get_water_quantity(), 30)

    def test_sellingItemsReducesQuantity(self):
        self.sale = BakeSale(1, 1, 1, 1)
        self.sale.sell_brownie(1)
        self.sale.sell_muffin(1)
        self.sale.sell_cake_pop(1)
        self.sale.sell_water(1)
        self.assertEqual(self.sale.get_brownie_quantity(), 0)
        self.assertEqual(self.sale.get_muffin_quantity(), 0)
        self.assertEqual(self.sale.get_cake_pop_quantity(), 0)
        self.assertEqual(self.sale.get_water_quantity(), 0)

    def test_notEnoughItemsWarningRaised(self):
        self.sale = BakeSale(1, 0, 0, 0)
        self.sale.not_enough_items_warning = MagicMock()
        self.sale.sell_brownie(2)
        self.sale.not_enough_items_warning.assert_called_once()

    def test_notEnoughStockWarningNotRaisedIfNotNeeded(self):
        self.sale = BakeSale(1, 0, 0, 0)
        self.sale.not_enough_items_warning = MagicMock()
        self.sale.sell_brownie(1)
        self.sale.not_enough_items_warning.assert_not_called()


if __name__ == '__main__':
    unittest.main()
