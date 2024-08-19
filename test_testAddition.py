import unittest
from testAddition import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')
    def test_difference(self):
        calculation = Calculations(10, 5)
        self.assertEqual(calculation.getDiifference(5))
if __name__ == '__main__':
    unittest.main()