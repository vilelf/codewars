import unittest
from maskify.main import maskify


class MainTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(maskify('1234567890'), '######7890')
        self.assertEqual(maskify('1234'), '1234')
        self.assertEqual(maskify(''), '')