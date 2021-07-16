class person:

    def set_name(self,name_var):
        self.name=name_var
    def get_name(self):
        return self.name
    def set_age(self,age_var):
        self.age=age_var
    def __get_age(self):
        return self.age
    

class student(person):
    cllg="dce"
    dept="cse"

    def get_cllg(self):
        return self.cllg
    def get_dept(self):
        return self.dept

class staff(student):
    sub="m1"
    def get_sub(self):
        return self.sub


tirumal=student()
tirumal.set_name("tirumal")
tirumal.set_age("21")
print(tirumal.get_name(),"of",tirumal.get_age(),"is in ",tirumal.get_cllg())

praveen=staff()
praveen.set_name("praveen")
praveen.set_age(22)
print(praveen.get_name(),"of age",praveen.get_age(),"teachin ",praveen.get_sub(),"in",praveen.cllg)

# otuput:
# tirumal of 21 is in  dce
# praveen of age 22 teachin  m1 in dce


