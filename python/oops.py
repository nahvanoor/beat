class Name:
    def sum(self,a,b):
        sum=a+b
        return sum
    
obj1=Name()
obj1.sum(1,2)
dir(obj1)
type(obj1)

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sum(self):
        sum=self.a+self.b
        return sum
    def difference(self):
        difference=self.a-self.b
        return difference
    def mul(self):
        mul=self.a*self.b
        return mul
    def div(self):
        div=self.a/self.b
        return div
    def quotient(self):
        quotient=self.a//self.b
        return quotient
    def remainder(self):
        remainder=self.a%self.b
        return remainder
    def square(self):
        square1=self.a**2
        square2=self.b**2
        return square1,square2
    def change(self,c,d):
        self.a=c
        self.b=d
cal=Calculator(10,5)
cal.sum()
cal.a
cal.b
cal.difference()
cal.mul()
cal.div()
cal.quotient()
cal.change(56,67)
cal.remainder()
cal.square()
dir(cal)

class Person:
    def demo(self):
        print("hello person")

class Student(Person):
    def demo1(self):
        print("hello student")

obj=Student()
dir(obj)
obj.demo()
obj.demo1()



#Write a Python class BankAccount with attributes like account_number, balance,date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited ${amount}.New balance is {self.balance}")
        else:
            print("amount should be valid")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"withdraw ${amount} . New balance is {self.balance}")
        else:
            print("insufficient balance or invalid amount")
    def check_balance(self):
        print(f"current balance : ${self.balance}")
    def account_details(self):
        print("----Account Details----")
        print("Account number : ",self.account_number)
        print("customer Name",self.customer_name)
        print("Balance",self.balance)
        print("Date of opening",self.date_of_opening)
        
acc=BankAccount(473898,0,"01/02/2010","nahva")
acc.deposit(10000)
acc.withdraw(5000)
acc.check_balance()
acc.account_details()
    

#Write a Python class Inventory with attributes like item_id, item_name, stock_count, and
#price, and methods like add_item, update_item, and check_item_details.
#Use a dictionary to store the item details, where the key is the item_id and the value is a
#dictionary containing the item_name, stock_count, and price.
class Inventory:
    def __init__(self,item_id,item_name,stock_count,price):
        self.item_id=item_id
        self.item_name=item_name
        self.stock_count=stock_count
        self.price=price
        self.item_details={}
        self.item_details[self.item_id]={"Item Name":self.item_name,"Stock count":self.stock_count,"Price":self.price}
    def add_item(self,id,name,stock,amount):
        if id not in self.item_details.keys():
            self.item_details[id]={"Item name":name,"stock":stock,"amount":amount}
            print("Current items after adding new item")
            print("Item Id\t\tItem Name\tStock Count\tPrice\n")
            for a,b in self.item_details.items():
                print(a,end="\t\t")
                for i,j in b.items():
                    print(j,end="\t\t")
                print()
        else:
            print("item id is already exist")
    def update_item(self,id,new_count):
        if id in self.item_details.keys():
            self.item_details[id]["Stock count"]+=new_count
            print(f"current stock count of ID : {id} ,item name : {self.item_details[id]["Item Name"]} is {self.item_details[id]["Stock count"]} ")
        else:
            print("item id is not exist")
    def check_item_details(self,id):
        if id in self.item_details.keys():
            print("---Item Details---")
            print("Item ID : ",id)
            for a,b in self.item_details[id].items():
                print(a,":",b)
item1=Inventory(1,"pen",10,5)
item1.add_item(2,"book",15,50)  
item1.update_item(1,15)  
item1.check_item_details(1)
    
#Write a Python class Restaurant with attributes like menu_items, book_table, and
#customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
#Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
class Restaurant:
    def __init__(self,menu_items,book_table,customer_orders):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_orders=customer_orders
        self.table_no=0
    def add_item_to_menu(self,item):
        if item not in self.menu_items:
            self.menu_items.append(item)
            print("menu : ",self.menu_items)
        else:
            print("item already exist")
    def book_tables(self,table_no):
        if table_no not in self.book_table:
            self.book_table.append(table_no)
            self.table_no=table_no
            print("Table",table_no, "has been reserved")
        else:
            print("Table" ,table_no, "is already booked")
    def customer_order(self,**order):
        if self.table_no>0:
                self.customer_orders[self.table_no]=order
                print("order taken")
                print("---customer order---")
                for a,b in order.items():
                    print(a,b)
    def display_menu(self):
        for i in self.menu_items:
            print(i)
cust1=Restaurant(["biriyani","mandhi"],[1,2,3,4],{})
cust1.add_item_to_menu("idly")
cust1.book_tables(int(input("please enter the table number for booking between 1-10: ")))
cust1.customer_order(biriyani=3,idly=2)
cust1.display_menu()
#Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and
#emp_department and methods like calculate_emp_salary, emp_assign_department, and
#print_employee_details.
#Sample Employee Data:
#"ADAMS", "E7876", 50000, "ACCOUNTING"
#"JONES", "E7499", 45000, "RESEARCH"
#"MARTIN", "E7900", 50000, "SALES"
#"SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
#which is the number of hours worked by the employee. If the number of hours worked
#is more than 50, the method computes overtime and adds it to the salary. Overtime is
#calculated as following formula:
#overtime = hours_worked - 50
#Overtime amount = (overtime * (salary / 50))
class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_departmnet):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_departmnet=emp_departmnet
    def calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime * (self.emp_salary/50))
            self.emp_salary+=overtime
            print(f"salary of employee is {self.emp_salary}")
        else:
            print(f"salary of employee is {self.emp_salary}")
    def emp_assign_department(self,new_department):
        self.emp_departmnet=new_department
        print(f"ID :{self.emp_id} {self.emp_name} is assigned to the department {new_department}")
    def print_emp_details(self):
        print(f"employee ID : {self.emp_id}")
        print(f"employee name : {self.emp_name}")
        print(f"employee salary : {self.emp_salary}")
        print(f"employee department : {self.emp_departmnet}")
emp1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2=Employee("JONES", "E7499", 45000, "RESEARCH")
emp3=Employee("MARTIN", "E7900", 50000, "SALES")
emp4=Employee("SMITH", "E7698", 55000, "OPERATIONS")
emp1.calculate_emp_salary(37)
emp1.emp_assign_department("RSEARCH")
emp1.print_emp_details()
emp3.calculate_emp_salary(60)
emp2.emp_assign_department("ACCOUNTING")
emp4.print_emp_details()



'''
Create a Python class Library with attributes like library_name, books, members, and methods like add_book, register_member, and issue_book.
Tasks:
Add new books to the library.
Register new members.
Issue books to members.
Print the list of books.
Print registered members.
Track issued books.
'''
class Library:
    def __init__(self,library_name,books,members):
        self.library_name=library_name
        self.books=books
        self.members=members
        self.issued_book={}
    def add_book(self,book_name):
       self.books.append(book_name)
       for a in self.books:
           print(a)
    def register_name(self,member_id,member_name):
        if member_id not in self.members:
            self.members[member_id]=member_name
            print("member",member_name,"registered")
        else:
            print("member id already exist")
    def issue_book(self,books,member_id):
        if books not in self.books:
            print("book does not exist")
        elif member_id not in self.members:
            print("member not found")
        else:
            self.issued_book[books]=member_id
            print("book is isssued to",self.members[member_id] )            
    def print_books(self):
        for a in self.books:
            print(a)
    def print_members(self):
        for a,b in self.members.items():
            print(a,":",b)   
    def print_issued_books(self):
        print("---Book issued to the members---")
        print("Books\t\tMembers ID\t\tMember name\n")
        for i,j in self.issued_book.items():
            print(i,"\t\t",j,"\t\t",self.members[j])
        print("------------------------------")
member1=Library("library",["alchemist"],{1:"Ranjinee"})
member1.add_book("harry potter")
member1.register_name(2,"nahva")
member1.issue_book("harry potter",1)
member1.print_books()
member1.print_members()
member1.print_issued_books()

