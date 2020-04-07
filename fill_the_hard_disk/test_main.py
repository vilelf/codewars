from unittest import TestCase
from fill_the_hard_disk.main import save


class FillTheHardDiskTest(TestCase):
    def test_main(self):
        self.assertEqual(save([4,4,4,3,3], 12), 3)
        self.assertEqual(save([4,4,4,3,3], 11), 2)
        self.assertEqual(save([4,8,15,16,23,42], 108), 6)
        self.assertEqual(save([13], 13), 1)
        self.assertEqual(save([1,2,3,4], 250), 4)
        self.assertEqual(save([100], 500), 1)
        self.assertEqual(save([11,13,15,17,19], 8), 0)
        self.assertEqual(save([45], 12), 0)

    def test_small_file_at_end_of_list(self):
        self.assertEqual(save([100, 100, 5], 10), 0)