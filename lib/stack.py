
class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def search(self, val):
        for i, v in enumerate(self.data):
            if v == val:
                return i, v
