import unittest

from rpn_converter import RPNConverter


class RPNConverterTest(unittest.TestCase):
    def setUp(self):
        self.rpn_conv = RPNConverter()

    def test_empty(self):
        self.assertEqual(self.rpn_conv.to_rpn(""), "")

    def test_whitespaces(self):
        self.assertEqual(self.rpn_conv.to_rpn("     \n\t\n\n\t\v\v\f\r\f\r\n    "), "")

    def test_digits_only(self):
        self.assertEqual(self.rpn_conv.to_rpn("12 3 1 43 5"), "")

    def test_validity_check(self):
        self.assertEqual(self.rpn_conv.check_validity("2 2 3 + *"), True)
        self.assertEqual(self.rpn_conv.check_validity(""), False)
        self.assertEqual(self.rpn_conv.check_validity("     \n\t\n\n\t\v\v\f\r\f\r\n    "), False)
        self.assertEqual(self.rpn_conv.check_validity("2 2 3 +"), False)
        self.assertEqual(self.rpn_conv.check_validity("2 2 2"), False)
        self.assertEqual(self.rpn_conv.check_validity("+ * - / / + "), False)


#         n + 1 operators means n operands for + - * /


if __name__ == '__main__':
    unittest.main()
