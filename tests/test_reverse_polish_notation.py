import unittest

from rpn_converter import RPNConverter


class RPNConverterTest(unittest.TestCase):
    def setUp(self):
        self.rpn_conv = RPNConverter()

    def test_empty(self):
        self.assertEqual(self.rpn_conv.to_rpn(""), None)


if __name__ == '__main__':
    unittest.main()
