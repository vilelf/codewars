from copy import copy


class SecureList(object):
    def __init__(self, secure_list):
        self.secure_list = copy(secure_list)

    def __getitem__(self, key):
        print(key)
        item = self.secure_list[key]
        self.secure_list.remove(item)
        return item

    def __repr__(self):
        list_ = str(self.secure_list)
        self.secure_list = []
        return list_

    def __len__(self):
        return len(self.secure_list)
