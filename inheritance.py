##
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self,fname,lname,course):
        super().__init__(fname,lname)
        self.course=course
    def display1(self):
        print(self.course)
        
obj=Student("pradeep1","k","python")
obj.display()




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
obj=GraduateStudent("alice",25,34656,"Machine Learning")
obj.display_graduate_info()



class Phone:
    def __init__(self):
        self.brand=""
        self.model=""
        self.price=""
class PhoneStore(Phone):
    def __init__(self):
        self.inventory=[]
    def add_phone(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.inventory.append((self.brand,self.model,self.price))
        print("Phone is added")
    def remove_phone(self,brand,model):
        count=0
        for i in self.inventory:
            if i[0]==brand and i[1]==model:
                self.inventory.remove(i)
                count+=1
                break
        if count==0:
            print("Phone not found")
        else:
            print("Phone is removed")
    def find_phone(self,brand,model):
        count=0
        for i in self.inventory:
            if i[0]==brand and i[1]==model:
                count+=1
                break
        if count==0:
            print("Phone not found")
        else:
            print("Phone is found",brand,model)
    def display_inventory(self):
        for i in self.inventory:
            print(i)
phone_store=PhoneStore()
while True:
    print("1. Add Phone to Inventory\n2. Remove Phone from Inventory\n3. Find Phone in Inventory\n4. Display Inventory\n5. Quit")
    choice=input("enter your choice")
    match choice:
        case "1":
            phone_store.add_phone(input("enter brand : "),input("enter model : "),input("enter price : "))
        case "2":
            phone_store.remove_phone(input("enter brand"),input("enter model"))
        case "3":
            phone_store.find_phone(input("enter brand"),input("enter model"))
        case "4":
            phone_store.display_inventory()
        case "5":
            break
        case _:
            print("invalid option")