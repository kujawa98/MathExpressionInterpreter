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
        self.assertEqual(self.rpn_conv.to_rpn("12 3 1 43 5"), ['12', '3', '1', '43', '5'])

    def test_operators_only(self):
        self.assertEqual(self.rpn_conv.to_rpn("* --+ //+*"), ['*', '-', '-', '/', '/', '+', '*', '+'])

    def test_expressions(self):
        self.assertEqual(self.rpn_conv.to_rpn("2 +2"), ['2', '2', '+'])
        self.assertEqual(self.rpn_conv.to_rpn("2 +3*4"), ['2', '3', '4', '*', '+'])
        self.assertEqual(self.rpn_conv.to_rpn("2+3*4/5-6/7+8"),
                         ['2', '3', '4', '*', '5', '/', '+', '6', '7', '/', '-', '8', '+'])

#         n + 1 operators means n operands for + - * /
#         we want RPN expression to evaluate to single number


if __name__ == '__main__':
    unittest.main()
