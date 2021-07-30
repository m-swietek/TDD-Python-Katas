import unittest


def add(number: str) -> str:
    if number == "":
        return "0"
    else:
        return number


class MyTestCase(unittest.TestCase):
    def test_emptyStringReturns0(self):
        self.assertEqual(add(""), "0")

    def test_oneNumberGetsReturned(self):
        self.assertEqual(add("1"), "1")
        self.assertEqual(add("1.1"), "1.1")


if __name__ == '__main__':
    unittest.main()
