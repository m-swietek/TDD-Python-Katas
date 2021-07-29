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
        self.totalToPay = 0.0
        self.amountPaid = 0.0
        self.browniesToSell = 0
        self.muffinsToSell = 0
        self.cakePopsToSell = 0
        self.watersToSell = 0

    def get_brownie_quantity(self) -> int:
        return self.brownieQuantity

    def get_water_quantity(self) -> int:
        return self.waterQuantity

    def get_cake_pop_quantity(self) -> int:
        return self.cakePopQuantity

    def get_muffin_quantity(self) -> int:
        return self.muffinQuantity

    def get_total_to_pay(self) -> float:
        return self.totalToPay

    def sell_brownie(self, quantity: int):
        if quantity > self.brownieQuantity:
            self.not_enough_items_warning()
        else:
            self.brownieQuantity -= 1

    def sell_muffin(self, quantity: int):
        if quantity > self.muffinQuantity:
            self.not_enough_items_warning()
        else:
            self.muffinQuantity -= 1

    def sell_cake_pop(self, quantity: int):
        if quantity > self.cakePopQuantity:
            self.not_enough_items_warning()
        else:
            self.cakePopQuantity -= 1

    def sell_water(self, quantity: int):
        if quantity > self.waterQuantity:
            self.not_enough_items_warning()
        else:
            self.waterQuantity -= 1

    def not_enough_items_warning(self):
        print("Not enough stock")

    def not_enough_money_warning(self):
        print("Not enough money")

    def parse_input(self, input_string: str):
        items_list = input_string.split(',')

        for item in items_list:
            if item == "B":
                self.browniesToSell += 1
                self.totalToPay += self.browniePrice
            elif item == "M":
                self.muffinsToSell += 1
                self.totalToPay += self.muffinPrice
            elif item == "C":
                self.cakePopsToSell += 1
                self.totalToPay += self.cakePopPrice
            elif item == "W":
                self.watersToSell += 1
                self.totalToPay += self.waterPrice

    def set_amount_paid(self, amount: float):
        self.amountPaid = amount

    def sell_items(self):
        if self.amountPaid >= self.totalToPay:
            if self.browniesToSell > 0:
                self.sell_brownie(self.browniesToSell)
                self.browniesToSell = 0

            if self.muffinsToSell > 0:
                self.sell_muffin(self.muffinsToSell)
                self.muffinsToSell = 0

            if self.cakePopsToSell > 0:
                self.sell_cake_pop(self.cakePopsToSell)
                self.cakePopsToSell = 0

            if self.watersToSell > 0:
                self.sell_water(self.watersToSell)
                self.watersToSell = 0
        else:
            self.not_enough_money_warning()


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

    def test_totalGetsCalculatedCorrectly(self):
        self.sale = BakeSale(1, 0, 1, 0)

        self.sale.parse_input('B,C')
        self.assertEqual(self.sale.get_total_to_pay(), 2.0)

    def test_mixedItemsRightAmountPaid(self):
        self.sale = BakeSale(1, 1, 1, 1)
        self.sale.sell_brownie = MagicMock()
        self.sale.sell_muffin = MagicMock()
        self.sale.sell_cake_pop = MagicMock()
        self.sale.sell_water = MagicMock()
        self.sale.not_enough_items_warning = MagicMock()

        self.sale.parse_input('B,C')
        self.sale.set_amount_paid(2.0)
        self.sale.sell_items()

        self.sale.sell_brownie.assert_called()
        self.sale.sell_muffin.assert_not_called()
        self.sale.sell_cake_pop.assert_called()
        self.sale.sell_water.assert_not_called()
        self.sale.not_enough_items_warning.assert_not_called()

    def test_mixedItemsNotEnoughMoneyPaid(self):
        self.sale = BakeSale(1, 1, 1, 1)
        self.sale.sell_brownie = MagicMock()
        self.sale.sell_muffin = MagicMock()
        self.sale.sell_cake_pop = MagicMock()
        self.sale.sell_water = MagicMock()
        self.sale.not_enough_money_warning = MagicMock()

        self.sale.parse_input('B,C')
        self.sale.set_amount_paid(1.5)
        self.sale.sell_items()

        self.sale.sell_brownie.assert_not_called()
        self.sale.sell_muffin.assert_not_called()
        self.sale.sell_cake_pop.assert_not_called()
        self.sale.sell_water.assert_not_called()
        self.sale.not_enough_money_warning.assert_called_once()


if __name__ == '__main__':
    unittest.main()
