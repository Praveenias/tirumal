class praveen:
    def print1(self):
        print("1")

class surya(praveen):
    def print1(self):
        super().print1()
        print("2")
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

deft = surya()
deft.add(1,2)
deft.add(1,2,3)
