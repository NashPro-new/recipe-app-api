"""
Sample tests
"""

from django.test import SimpleTestCase  #using this as this is a test without database

from app import calc

class CalcTests(SimpleTestCase):
    """Test the Calc module."""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5,6)

        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(7,8)    #inputs

        self.assertEqual(res, -1)    #assert equal to check input gives output we need