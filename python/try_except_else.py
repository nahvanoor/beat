
try:
    int(input("hello pls enter a number"))
except :
    print("pls enter correct number")
    int(input())

    
while True:
    try:
        int(input())
    except:
        print("gjhg")
    else:
        break 
    
    
#calculator      
print("CALCULATOR")
print("----------------") 
while True:
    print("1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n5.exit") 
    while True:
        try: 
            op=int(input("please enter the operation"))
            num1=int(input("enter first number"))
            num2=int(input("enter second number"))
        except:
            print("please enter correct number")
        else:
            break
    result=0
    match op:
        case 1:
            result=num1+num2
            print("sum : ",result)
        case 2:
            result=num1-num2
            print("difference : ",result)
        case 3:
                result=num1*num2
                print("product : ",result)
        case 4:
            while True:
                try:
                    result=num1/num2
                except:
                    ("please enter the denominator greater than zero")
                    num2=int(input())
                else:
                    print("result : ",result)
                    break
        case _:
            print("please choose valid operation")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print("Name : ",self.name,"\nAge :",self.age)
class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id=student_id
    def display_student_info(self):
        self.display_info()
        print("Student ID : ",self.student_id)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id,research_topic):
        super().__init__(name, age, student_id)
        self.research_topic=research_topic
    def display_graduate_info(self):
        self.display_student_info()
        print("Research topic : ",self.research_topic)
name=input("enter your name : ")
while True:
    try:
        age=int(input("enter your age : "))
    except:
        print("Please enter the correct age")
    else:
        break
student_id=input("enter your student_id : ")
research_topic=input("enter your research topic")
obj=GraduateStudent("alice",25,34656,"Machine Learning")
obj1=GraduateStudent(name,age,student_id,research_topic)
obj.display_graduate_info()
obj1.display_graduate_info()

