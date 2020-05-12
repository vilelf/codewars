from unittest import TestCase
from multiplication_table.main import multiplication_table


class MainTest(TestCase):
    def test_quando_dado_3(self):
        actual = multiplication_table(3)
        expected = [[1,2,3],[2,4,6],[3,6,9]]
        self.assertEqual(actual, expected)

    def test_quando_dado_4(self):
        actual = multiplication_table(4)
        expected = [[1,2,3,4],[2,4,6,8],[3,6,9,12], [4,8,12,16]]
        self.assertEqual(actual, expected)

    def test_quando_dado_0(self):
        actual = multiplication_table(0)
        expected = []
        self.assertEqual(actual, expected)
