import unittest


def add(number: str) -> str:
    if number == "":
        return "0"
    else:
        numbers_split = number.split(',')

        if len(numbers_split) == 1:
            return number
        else:
            numbers_sum = 0

            for x in numbers_split:
                numbers_sum += float(x)

            if numbers_sum.is_integer():
                return str(int(numbers_sum))
            else:
                return str(numbers_sum)


class MyTestCase(unittest.TestCase):
    def test_emptyStringReturns0(self):
        self.assertEqual(add(""), "0")

    def test_oneNumberGetsReturned(self):
        self.assertEqual(add("1"), "1")
        self.assertEqual(add("1.1"), "1.1")

    def test_numbersSeparatedByCommaGetAdded(self):
        self.assertEqual(add("1,2"), "3")
        self.assertEqual(add("1,2,3"), "6")
        self.assertEqual(add("1.1,2.3,3.5"), "6.9")


if __name__ == '__main__':
    unittest.main()
