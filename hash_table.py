class Hash():
    def __init__(self):

        self.size = 10
        self.hash = [None] * self.size

    def hashing(self, key):
        if key < self.size:
            return key
        else:
            return key %  self.size

    def add(self, key, value):
        key = self.hashing(key)
        self.hash[key] = value

    def lookup(self, key):
        key = self.hashing(key)
        return self.hash[key]

h = Hash()
h.add(10, [1,2,4,5])
h.add(1, 'pranav')
print(h.lookup(10))

