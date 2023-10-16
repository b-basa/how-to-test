import unittest
from src.some_module import some_math_function, some_file_operation_function

# Unittest is built in and comes installed with Python.
# It is a very simple to use test suite and could be used for smaller projects.
# Has several methods for testing like assertEquals, assertTrue, assertRaises etc...


class UnitTestExamples(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        # setUpClass is a special method in unittest that lets you define parameters
        # that can be used in all tests. You can read a csv, precalculate things etc...
        self._a = 5
        self._b = 10

    def test_some_math_function_(self):
        self.assertEqual(some_math_function(self._a, self._b), 9765630)

    def test_some_file_operation_function_(self):
        raise NotImplementedError()
