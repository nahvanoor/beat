class Person:
    def display(self):
        print("person")
        
class Student(Person):
    def display(self):
        print("student")
person=Person()        
student=Student()
person.display()
student.display()




#local and global variable
class Person:
    count1=0
    def display(self,model):
        print("I am Person",self.count1,model)
        print(locals())
class Student(Person):
    def display(self):
        print("I am Student")
        print(globals())
        
person=Person()
student=Student()
person.display("hi")
student.display()

Person.count1
person.count1

count1=0
def display(count1):
        print("I am Person",count1)
        print(locals())
display(count1)
for value in [person,student]:
    value.display()