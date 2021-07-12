class suryarray:
    def __init__(self, a):
        self.a = a

    def append(self, val):
        self.a.append(val)

    def remove(self, val):
        self.a.remove(val)

    def count(self, val):
        return self.a.count(val)

    def pop(self):
        self.a.pop()

    def display(self):
        return self.a


l1=suryarray([1,2,3])
print(l1.display())
l1.append(4)
print(l1.display())
l1.append(1)
print(l1.display())
print(l1.count(1))
l2=suryarray([4,5,6])
print(l2.display())
l2.pop()
print(l2.display())