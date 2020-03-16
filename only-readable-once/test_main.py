from unittest import TestCase
from main import SecureList


base = [1,2,3,4]
class SecureListTest(TestCase):

    def test_receives_a_list_on_init(self):
        secure_list = SecureList([])
        self.assertEquals([], secure_list.secure_list)
        
    def test_get_element(self):
        secure_list = SecureList(base)
        self.assertEquals(secure_list.secure_list[0], base[0])

    def test_element_is_removed(self):
        secure_list = SecureList(base)
        self.assertEquals(secure_list.secure_list[0], base[0])
        self.assertEquals(secure_list.secure_list[0], base[1])

    def test_class_must_return_len(self):
        secure_list = SecureList([1,2,3])
        self.assertEquals(len(secure_list), 3)

    def test_clean_list_after_print(self):
        secure_list = SecureList([1,2,3])
        secure_list.__repr__()
        self.assertEquals(len(secure_list), 0)
