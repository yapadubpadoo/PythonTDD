import unittest
from fizzbuzz import FizzBuzz


class TestNumberToString(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_1_when_number_is_1(self):
        self.assertEqual('1', self.fizzbuzz.count(1))

    def test_it_should_return_2_when_number_is_2(self):
        self.assertEqual('2', self.fizzbuzz.count(2))


class TestNumberToFizz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_fizz_when_number_is_3(self):
        self.assertEqual('fizz', self.fizzbuzz.count(3))

    def test_it_should_return_fizz_when_number_is_6(self):
        self.assertEqual('fizz', self.fizzbuzz.count(6))


class TestNumberToBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_buzz_when_number_is_5(self):
        self.assertEqual('buzz', self.fizzbuzz.count(5))

    def test_it_should_return_buzz_when_number_is_10(self):
        self.assertEqual('buzz', self.fizzbuzz.count(10))


class TestNumberToFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_it_should_return_fizzbuzz_when_number_is_15(self):
        self.assertEqual('fizzbuzz', self.fizzbuzz.count(15))
