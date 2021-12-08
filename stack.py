# STACK:(List)
#
# -->LIFO  -->(algorith)

STACKSIZE=5
# APPEND()
# POP()-->DEFAULT:REMOVE LAST VALUE
# NUMBER OF VALUES
# isfilled()
#
# ALERT:
#
# Stackoverflow -->when stack is filled and we try to insert
#
# stackunderflow --> when we pop in empty stack
#
# STACKSIZE=5
#
# append(2) -[2]
# append(3) -[2,3]
# append(4) -[2,3,4]
# pop() -[2,3]
# isfilled() --> false
# pop()
# pop()
# pop() -->stackunderflow alert

class stackk:
    def __init__(self,size):
        self.stack_list=[]
        self.stack_size=size
    def insert_list(self,num):
        if self.stack_size == self.lenght_of_stack():
            print("overflow")
        else:
            self.stack_list.append(num)

    def pop_list(self):
        if self.lenght_of_stack() == 0:
            print("underflow")
        else:
            self.stack_list.pop()

    def lenght_of_stack(self):
        return len(self.stack_list)

    def display(self):
        print(self.stack_list)


stack_obj=stackk(5)
l1=[1,2,3,4,5]
for i in l1:
    stack_obj.insert_list(i)
stack_obj.display()
stack_obj.insert_list(6)
for i in range(stack_obj.lenght_of_stack()):
    stack_obj.pop_list()
stack_obj.display()
stack_obj.pop_list()


# output:






