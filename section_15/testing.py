import unittest
import main


class TestMain(unittest.TestCase):

    def test_input_correct(self):
        guess = 5
        answer = 5
        correct_guess = main.run_guess(guess, answer)
        self.assertTrue(correct_guess)

    def test_input_incorrect_low(self):
        guess = 5
        answer = 1
        incorrect_guess = main.run_guess(guess, answer)
        self.assertFalse(incorrect_guess)

    def test_input_incorrect_high(self):
        guess = 5
        answer = 10
        incorrect_guess = main.run_guess(guess, answer)
        self.assertFalse(incorrect_guess)

    def test_input_wrong_type(self):
        guess = "sdfsdf"
        self.assertRaises(ValueError, main.validate_int, guess)


if __name__ == '__main__':
    unittest.main()
