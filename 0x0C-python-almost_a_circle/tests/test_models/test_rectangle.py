#!/usr/bin/env python3


"""Test module for rectangle class"""

import unittest
import pep8
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test pep8 style"""
    def test_pep8_conformance(self):
        """check pep8 style compliance"""
        pep8Style = pep8.StyleGuide(quiet=True)
        result = pep8Style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """reset Base instances count"""
        Base._Base__nb_objects = 0

    def test_width_height_input(self):
        """Use of width and height"""
        rect1 = Rectangle(10, 2)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)

    def test_ValueError_input(self):
        """value error """
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -2, 2)
        self.assertRaises(ValueError, Rectangle, 1, 1, 2, -3)
       
    def test_x_y_input(self):
        """using position with X and Y correct values"""
        rect = Rectangle(1, 1, 2, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)
        rect2 = Rectangle(1, 1, 0, 0)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)

    def test_instance_id(self):
        """check multiple instance id"""
        rect1 = Rectangle(1,1)
        rect2 = Rectangle(2,1)
        rect3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect3.id, 12)

    def test_inheritance(self):
        """Check rectangle inheritance from base class"""
        rect = Rectangle(1,1)
        self.assertIsInstance(rect, Base)
        self.assertIsInstance(rect, Rectangle)

    def test_area_value(self):
        """check area of rectangle value"""
        rect = Rectangle(2,2)
        self.assertEqual(rect.area(), 4)
        rect2 = Rectangle(3, 2)
        self.assertEqual(rect2.area(), 6)
        rect3 = Rectangle(2, 10)
        self.assertEqual(rect3.area(), 20)
        rect4 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect4.area(), 56)

    def test_stdout_representation(self):
        """check if rectangles string rep is exact"""
        str2x3 = "##\n##\n##\n"
        rect = Rectangle(2, 3)
        temp_out = StringIO()
        sys.stdout = temp_out
        rect.display()
        self.assertEqual(temp_out.getvalue(), str2x3)
        temp_out.close()
        temp_out2 = StringIO()
        sys.stdout = temp_out2
        str4x6 = "####\n####\n####\n####\n####\n####\n"
        rect1 = Rectangle(4, 6)
        rect1.display()
        self.assertEqual(temp_out2.getvalue(), str4x6)

    def test_str_representation(self):
        """__str__ format: [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_position(self):
        """Print rectangle transposed by x and y"""
        str2x3 = "\n\n  ##\n  ##\n  ##\n"
        rect = Rectangle(2, 3, 2, 2)
        temp_out = StringIO()
        sys.stdout = temp_out
        rect.display()
        self.assertEqual(temp_out.getvalue(), str2x3)
        temp_out.close()
        temp_out2 = StringIO()
        sys.stdout = temp_out2
        str4x6 = " ###\n ###\n"
        rect1 = Rectangle(3, 2, 1, 0)
        rect1.display()
        self.assertEqual(temp_out2.getvalue(), str4x6)
        temp_out2.close()

    def test_update_0(self):
        """Check updating multiple non-keyworded arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_1(self):
        """check updating multiple keyworded arguments"""
if __name__ == "__main__":
    unittest.main()
