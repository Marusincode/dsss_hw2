import unittest
from math_quiz import randomise_integer, randomise_operator, operation

class TestMathGame(unittest.TestCase):

    def test_randomise_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomise_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, 
                            f"Random number {rand_num} is out of range [{min_val}, {max_val}]")

    def test_randomise_operator(self):
        """
        Test if the generated operator is in the specified list.
        """
        choice = ['+', '-', '*']

        for _ in range(1000):
            operator = randomise_operator()
            self.assertIn(operator, choice, 
                          f"Operator '{operator}' is not valid")

    def test_operation(self):
        """
        Test if the generated problems and answers match the test cases.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (9, 6, '-', '9 - 6', 3),
            (9, 3, '*', '9 * 3', 27),
            (8, 0, '+', '8 + 0', 8),
            (2, 2, '-', '2 - 2', 0),
            (6, 7, '*', '6 * 7', 42)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem, 
                            f"Generated problem '{problem}' doesnt match '{expected_problem}'")
            self.assertEqual(answer, expected_answer, 
                            f"Answer '{answer}' doesnt match '{expected_answer}'")

if __name__ == "__main__":
    unittest.main()
