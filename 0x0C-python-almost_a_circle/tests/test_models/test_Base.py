#!/usr/bin/python3
"""
Set of tests for base class
"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for base class including style and id input"""
    def SetUp(self):
        """reset base instances count"""
        Base._Base__nb_objects = 0

    def test_pep8_style(self):
        """checkl pep8 style"""
        basePep8Style = pep8.StyleGuide(quiet=True)
        result = basePep8Style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "base file has pep8 style errors or warnings")

    def test_ids(self):
        """Check base instances ids"""
        rect1 = Base()
        self.assertEqual(rect1.id, 1)
        rect2 = Base()
        self.assertEqual(rect2.id, 2)
        rect3 = Base(3)
        self.assertEqual(rect3.id, 3)
        rect4 = Base()
        self.assertEqual(rect4.id, 4)

    def test_multiple_args_to_base(self):
        """Check if base object defined with multiple arguments"""
        self.assertRaises(TypeError, Base, 2, "hola")


if __name__ == "__main__":
    unittest.main()
