import unittest
from fizzbuzz import Fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(Fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(Fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(Fizzbuzz(15), "FizzBuzz")

    def test_numbeer(self):
        self.assertEqual(Fizzbuzz(7), '7')

if __name__ == '__main__':
    unittest.main()
