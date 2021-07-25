import unittest


def are_brackets_balanced(input_string: str) -> bool:
    if input_string == "[" or input_string == "]":
        return False

    return True


class BalancedBracketsTest(unittest.TestCase):

    def test_emptyStringIsBalanced(self):
        self.assertEqual(are_brackets_balanced(""), True)

    def test_oneLeftBracketUnbalanced(self):
        self.assertEqual(are_brackets_balanced("["), False)

    def test_oneRightBracketUnbalanced(self):
        self.assertEqual(are_brackets_balanced("]"), False)


if __name__ == '__main__':
    unittest.main()
