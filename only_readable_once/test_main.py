from unittest import TestCase
from only_readable_once.main import SecureList


base = [1,2,3,4]
class SecureListTest(TestCase):
    def test_get_element(self):
        secure_list = SecureList(base)
        self.assertEqual(secure_list[0], base[0])

    def test_element_is_removed(self):
        secure_list = SecureList(base)
        _ = secure_list[0]
        self.assertNotIn(1, secure_list)

    def test_class_must_return_len(self):
        secure_list = SecureList([1,2,3])
        self.assertEqual(len(secure_list), 3)

    def test_clean_list_after_print(self):
        secure_list = SecureList([1,2,3])
        secure_list.__repr__()
        self.assertEqual(len(secure_list), 0)
