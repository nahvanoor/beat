def sum():
    a=1
    b=4
    print(a+b)
sum()

def sum(a,b):
    print(a+b)
sum(1,4)


def pattern():
    for row in range(1,6):
        for col in range(0,row):
            print("*",end="")
        print("")
pattern()


def flower_list(x):
    value=0
    while value<len(x):
        print(x[value])
        value+=1
flower_list(["lilly","rose","tulip"])


def vowels(x,v):
    count=0
    for i in x:
        if i in v:
            count=count+1
    return count
vowels("she is beautiful",['a','e','i','o','u'])


def multiplication_table(n):
    for i in range(1,11):
        print(f"{i} X {n}={i*n}")
multiplication_table(5)

def division_table(n):
    for i in range(1,11):
        print(f"{i} / {n}={i/n}")
division_table(5)
        




#1        
def sum_list(x):
    sum=0
    for i in x:
        sum=sum+i
    print(sum)
sum_list([23,34,45,56])



#2
def largest_no(x):
    largest=0
    for i in x:
        if i > largest:
            largest=i
    print(largest)
largest_no([56,78,37,46])


def largest_no(x):
    x.sort()
    print(x[-1])
largest_no([56,78,37,46])


#3
def count_strings(x):
    count=0
    for i in x:
        if len(i)>=2:
            if i[0]==i[-1]:
                count=count+1
    print(count)
count_strings(['abc','aba','121','4324'])



#4
def remove_duplicates(x):
    for i in x:
        if x.count(i)>=2:
            x.remove(i)
    print(x)
remove_duplicates(['apple','banana','grapes','apple','grapes'])



#5
def check_list(x):
    if len(x)==0:
        print("list is empty")
    else:
        print("list is not empty")
check_list([])
            
            
            
#6
def copy_list(x):
    list2=x.copy()
    print(list2)
copy_list(['abc','xyz','123'])


#7
def list1():
    listsquare=[]
    for i in range(1,31):
        listsquare.append(i*i)
    print(listsquare)
    print("First 5 elements" ,listsquare[:5])
    print("Last 5 elements",listsquare[-5:])
list1()


#8
def list_index(x):
    list1=[]
    for i in x:
        list1.append(x.index(i))
    print(list1)
list_index([23,34,45,56])


#9
def unique_value(x):
    list1=[]
    for i in x:
        if x.count(i)==1:
            list1.append(i)
    print(list1)
unique_value(['apple','banana','grapes','apple','grapes'])


#10
def common_value():
    list1=['apple','banana','orange','grapes']
    list2=['orange','kiwi','mango','apple']
    list3=[]
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i]==list2[j]:
                list3.append(list1[i])
    print(list3)
common_value()
                
        
    
        
def common_value(l1,l2):
    l3=[]
    i=0
    while i<len(l1):
        j=0
        while j<len(l2):
            if l1[i]==l2[j]:
                if l1[i] not in l3:
                    l3.append(l1[i])
            j+=1
        i+=1
    print(l3)
    print(set(l1).intersection(l2))
common_value(['apple','banana','orange','grapes'],['orange','kiwi','mango','apple','apple'])


def common_value(l1,l2):
        print(set(l1).intersection(l2))
        
common_value(['apple','banana','orange','grapes'],['orange','kiwi','mango','apple','apple'])



def mul_div():
    list1=[]
    list2=[]
    for i in range(1500,2700):
        if i%7==0:
            list1.append(i)
        elif i%5==0:
            list2.append(i)
    print(list1)
    print(list2)
mul_div()


def number_guess():           
    import random     
    number=int(input("guess a number: "))
    x=random.randint(1,20)
    while number!=x:
        number=int(input("wrong! guess again : "))
    print("well guessed!")
number_guess()


def fizzbuzz():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)
fizzbuzz()



import math
def area_circle():
    r=float(input("enter the radius of the circle : "))
    area=math.pi*(r**2)
    print("radius=",r)
    print("area=",area)
area_circle()


def name():
    fname=input("enter your first name : ")
    lname=input("enter your last name : ")
    reversed=lname + " " + fname
    print(reversed)
name()



def name():
    fname=input("enter your first name : ")
    lname=input("enter your last name : ")
    print("reversed name = ",lname,fname)
name()


def list_tuple():
    input_str = input("Enter comma-separated numbers: ") 
    num_list=input_str.split(',')
    num_tuple = tuple(num_list)
    print("List :", num_list)
    print("Tuple :", num_tuple)
list_tuple()



def file():
    filename=input("enter the file name : ")
    extension=filename.split('.')[-1]
    return extension
file()


def sum_mul():
    n=input("enter a number : ")
    result=int(n)+int(n+n)+int(n+n+n)
    print("result= ",result)
sum_mul()


def equal():
    a=int(input("entre a number : "))
    b=int(input("entre a number : "))
    c=int(input("entre a number : "))
    sum=a+b+c
    if a==b==c:
        sum=sum*3
        print(sum)
    else:
        print(sum)
equal()


def equal():
    a=int(input("entre a number : "))
    b=int(input("entre a number : "))
    c=int(input("entre a number : "))
    if a==b==c:
        sum=3*a
    else:
        sum=a+b+c
    return sum
print(equal())
a=equal()
a*5
def equal():
    a=int(input("entre a number : "))
    b=int(input("entre a number : "))
    c=int(input("entre a number : "))
    sum=a+b+c
    if a==b or b==c or a==c:
        sum=0
        print(sum)
    else:
        print(sum)
equal()
name="pradeep.kfhfyf"
name.index('.')
name[name.index('.')+1:]


def digit():
    num=input("enter number")
    print(len(num))
digit()


def list_sum(*x):
    sum=0
    print(x)
    for i in x:
        sum+=i
    return sum
list_sum(1,2,3,4)


def upper_name():
    name=["abc","sdr","xyz"]
    name_upper=[]
    for i in name:
        name_upper.append(i.upper())
    return name_upper
upper_name()

person={"name":"nahva","age":21,"place":"malappuram"}
key=person.keys()
for i in key:
    print(person[i])



def prime(num):
    if num==2:
        print("it is prime") 
    else:   
        for i in range(2,num//2+1):
            if num%i==0:
                break
        if i==num-1:
            print("it is prime")
        else:
            print("it is not prime")
prime(4)




num="1634"
sum=0
for i in num:   
    num2=[]
    num2.append(int(i)**len(num))
    for j in num2:
        sum=sum+j
if sum==int(num):
    print("it is armstrong")
else:
    print("it is not armstrong")
    
    
    
    
def armstrong(num):
    string_number=str(num)
    armstrong=0
    for i in string_number:
        armstrong+=int(i)**len(string_number)
    if num==armstrong:
        return "it is armstrong"
    else:
        return "it is not armstrong"
armstrong(1634)




def prime(num):
    if num==2:
        print("it is prime")
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                break
        if i==num//2:
            print("it is prime")   
        else:
            print("it is not prime") 
prime(13)


def not_prime(a,b):     
    for j in range(a,b+1):
        if j==1:
            print(j)     
        else:
            for i in range(2,j//2+1):
                if j%i==0:
                    print(j)
                    break
not_prime(1,50)



def square(list1):
    square_list=[]
    for i in list1:
        square_list.append(i**2)
    return square_list
square1=square([1,2,3,4,5,6,7,8,9])   
print(square1)


