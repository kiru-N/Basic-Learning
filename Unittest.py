import unittest
import main



class TestMain(unittest.TestCase):
	def test_check_sum(self):
		value = 0
		result = main.test_sum(value)
		self.assertNotEqual(result, 5)

	def test_check_sum2(self):
		value = 'sdfdf'
		result = main.test_sum(value)
		self.assertIsInstance(result, ValueError)

	def test_check_sum3(self):
		value = None
		result = main.test_sum(value)
		self.assertEqual(result, 'Please Enter Number')

	def test_check_sum4(self):
		value = ''
		result = main.test_sum(value)
		self.assertEqual(result, 'Please Enter Number')

if __name__ == '__main__':
	unittest.main()
