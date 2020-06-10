#!/usr/bin/env python3

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareClass(unittest.TestCase):
    """CLass to test square methods"""

    def setUp(self):
        """Reset base instance count for each test"""
        Base._Base__nb_objects = 0

    def test_square_pep8_style(self):
        """Verify Square module style"""
        pep8Style = pep8.StyleGuide(quiet=True)
        result = pep8Style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_inheritance(self):
        """check square inheritance of base"""

    def test_string_rep_overload(self):
        """Verify __str__ method format for Squares"""
