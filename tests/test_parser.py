import unittest
from parser_ import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser_ = Parser()

    def test_empty(self):
        self.assertEqual(self.parser_.parse([]), None)


if __name__ == '__main__':
    unittest.main()
