from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """tests the calculator module"""

    def test_add_numbers(self):
        """tests the number addition"""
        res = calc.add(6, 4)
        self.assertEqual(res, 10)
