import unittest

from rpn_converter import RPNConverter


class RPNConverterTest(unittest.TestCase):
    def setUp(self):
        self.rpn_conv = RPNConverter()

    def test_empty(self):
        self.assertEqual(self.rpn_conv.to_rpn(""), None)

    def test_whitespaces(self):
        self.assertEqual(self.rpn_conv.to_rpn("     \n\t\n\n\t\v\v\f\r\f\r\n    "), None)

    def test_digits_only(self):
        self.assertEqual(self.rpn_conv.to_rpn("12 3 1 43 5"), "12 3 1 43 5")


if __name__ == '__main__':
    unittest.main()
