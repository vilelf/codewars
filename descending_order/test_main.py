from unittest import TestCase
from descending_order.main import descending_order


class MainTest(TestCase):
    def test_main(self):
        self.assertEqual(descending_order(1234), 4321)
        self.assertEqual(descending_order(1243), 4321)
        self.assertEqual(descending_order(515), 551)
