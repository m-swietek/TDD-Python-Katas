import unittest


def are_brackets_balanced(input_string: str) -> bool:
    return True


class BalancedBracketsTest(unittest.TestCase):

    def test_emptyStringIsBalanced(self):
        self.assertEqual(are_brackets_balanced(""), True)


if __name__ == '__main__':
    unittest.main()
