class SecureList(object):
    def __init__(self, slist):
        self._list = slist[:]

    def __getitem__(self, key):
        return self._list.pop(key)

    def __repr__(self):
        temp, self._list = self._list, []
        return repr(temp)

    def __str__(self):
        temp, self._list = self._list, []
        return str(temp)

    def __len__(self):
        return len(self._list)
