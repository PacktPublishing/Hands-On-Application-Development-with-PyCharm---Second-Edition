# This is a unit test that proves the test in the above frame works.

from unittest import TestCase
from main import add_two_numbers

class Test(TestCase):
    def test_add_two_numbers(self):
        self.assertTrue(add_two_numbers(a=5, b=6) == 11, "Should be 11")

    def test_show_a_fail(self):
        self.fail()
