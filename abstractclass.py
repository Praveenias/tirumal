from abc import ABC, abstractmethod
class human(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def leg_count(self):
        pass
    
    def hand_count(self):
        pass
class sapiens(human):
    def print1(self):
        print("in sapiens")
    def name(self):
        print("in sapiens")
    def leg_count(self):
        print("2 legs")
class homo_sapiens(human):
    def name(self):
        print("in homo_sapiens")
    def print1(self):
        print("in homo_sapiens")
    def leg_count(self):
        print("2 legs")

gan=sapiens()
gan.leg_count()


##is instance and is sub_class

class one:
    pass
class two(one):
    pass
class three:
    pass

o=one()
b=three()
print(isinstance(b,one))
print(issubclass(two,one))
