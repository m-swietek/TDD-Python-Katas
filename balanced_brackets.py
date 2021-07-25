import unittest


def are_brackets_balanced(input_string: str) -> bool:
    left_brackets_to_balance = 0

    for bracket in input_string:
        if bracket == "[":
            left_brackets_to_balance += 1
        elif bracket == "]":
            left_brackets_to_balance -= 1

    if left_brackets_to_balance == 0:
        return True
    else:
        return False


class BalancedBracketsTest(unittest.TestCase):

    def test_emptyStringIsBalanced(self):
        self.assertEqual(are_brackets_balanced(""), True)

    def test_oneLeftBracketUnbalanced(self):
        self.assertEqual(are_brackets_balanced("["), False)

    def test_oneRightBracketUnbalanced(self):
        self.assertEqual(are_brackets_balanced("]"), False)

    def test_oddBracketsStringIsUnbalanced(self):
        self.assertEqual(are_brackets_balanced("[][]["), False)


if __name__ == '__main__':
    unittest.main()
