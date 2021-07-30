import unittest


def add(number: str) -> str:
    return "0"


class MyTestCase(unittest.TestCase):
    def test_emptyStringReturns0(self):
        self.assertEqual(add(""), "0")


if __name__ == '__main__':
    unittest.main()
