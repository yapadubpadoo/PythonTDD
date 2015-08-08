import unittest
from app import app


class TestFizzBuzzAPI(unittest.TestCase):
	def test_root(self):
		self.app = app.test_client()
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('Hello world!', response.data)

	def test_fizzbuzz_3_return_fizz(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/3')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('fizz', response.data)

	def test_fizzbuzz_1_return_1(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/1')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('1', response.data)

	def test_fizzbuzz_5_return_buzz(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/5')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('buzz', response.data)

	def test_fizzbuzz_10_return_buzz(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/10')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('buzz', response.data)

	def test_fizzbuzz_15_return_buzz(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/15')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('fizzbuzz', response.data)