

def square(list1):
    square_list=[]
    for i in list1:
        square_list.append(i**2)
    return square_list
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
id(list1[0])
square(list1)
    
def square1(list1):
    for i in list1:
        yield i**2

list(square1(list1))
for value in square1(list1):
    print(value)

name="pradeep"
a=iter(name)
next(a)

list6=[1,2,3,4,5]
list7=[]
for value in list6:
    list7.append(value**2)
list7
def square(a):
    return a**2

list(map(square,list6))
list(map(lambda a:a**2,list6))



list1=['nahva','ranjinee','kamaru']
def upper(i):
    return i.upper()

list(map(upper,list1))


list(map(lambda i:i.upper(),list1))




def sum(num):
    sum=0
    for i in num:
        sum=sum+i
    return sum
sum([23,34,56,45,67,78])




from functools import reduce
def result(a,b):
    return a+b
values=[23,34,56,45,67,78]
reduce(result,values)
reduce(lambda a,b:a+b,values)


def maxx(a,b):
    if a>b:
        return a
    else:
        return b
    
reduce(maxx,values)
reduce(lambda a,b:a if a>b else b,values)



#Write a Python program to find if a given string starts with a given character using Lambda.
#1
def start_with(s,c):
    if s[0]==c:
        return True
    else:
        return False
s="hello"
c="h"
start_with(s,c)

#2
same=lambda a,b: True if a[0]==b else False
print(same("hello","H"))



#Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
#1
def sum_length(name):
      sum=0
      for i in name:
          sum=sum+len(i)
      return sum
names=["Alice", "Bob", "Charlie", "david"]
upper_names=list(filter(lambda i:i[0].isupper(),names))  
sum_length(upper_names)  
  
#2
from functools import reduce
names=["Alice", "Bob", "Charlie", "david"]
upper_names=list(filter(lambda i:i[0].isupper(),names))
reduce(lambda a,b: a+len(b),upper_names,0)

#3
names=["Alice", "Bob", "Charlie", "david"]
total_length=sum(map(len,filter(lambda i:i[0].isupper(),names)))
print(total_length)


#Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
#1
numbers=[-1,2,3,-4,-5,6]
positive_numbers=filter(lambda i:i>0,numbers)
negative_numbers=filter(lambda i:i<0,numbers)
pos_sum=0
for i in positive_numbers:
    pos_sum=pos_sum+i
print(pos_sum)
neg_sum=0
for j in negative_numbers:
    neg_sum=neg_sum+j
print(neg_sum)

#2
numbers=[-1,2,3,-4,-5,6]
positive_numbers=sum(filter(lambda i:i>0,numbers))
negative_numbers=sum(filter(lambda i:i<0,numbers))
print("positive numbers : ",positive_numbers)
print("nrgative numbers : ",negative_numbers)


#Write a Python program to add two given lists using map and lambda.
list1=[1,2,3,4]
list2=[2,4,6,8]
list3=list(map(lambda a,b:a+b,list1,list2))
print(list3)
    


#Write a Python program to create Fibonacci series up to n using Lambda





#Write a Python program that uses a lambda function to extract even numbers from a list
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda i:i%2==0,numbers))
print("even numbers: ",even_numbers)


#Write a Python program using lambda and filter() to count how many words in a list start with a given letter.
#1
fruits=["apple", "banana", "avocado", "apricot", "berry"]
letter='a'
count=sum(map(lambda a:a[0]==letter,fruits))
print("count of fruits start with letter a: ",count)


#2
fruits=["apple", "banana", "avocado", "apricot", "berry"]
letter='a'
count=sum(map(lambda a:a.startswith(letter),fruits))
print("count of fruits start with letter a: ",count)
#3
fruits=["apple", "banana", "avocado", "apricot", "berry"]
count=sum(list(filter(lambda a:a[0]=='a',fruits)))
print("count of fruits start with letter a: ",count)


#Write a Python program to find the longest string in a list using reduce() and a lambda function.
fruits=["apple", "banana", "avocado", "apricot", "berry"]
long_string=reduce(lambda a,b:a if len(a)>len(b) else b,fruits)
print("longest string: ",long_string)


#Write a Python program using a lambda function and filter() to extract all palindromes from a given list of strings
words = ["mom", "apple", "level", "banana", "noon", "python"]
reverse=list(filter(lambda a:a==a[::-1],words))
print("palindrome : ",reverse)


#Write a Python program using map() and a lambda function to capitalize the first letter of each word in a list.
#1
fruits=["apple", "banana", "avocado", "apricot", "berry"]
new_list=list(map(lambda a:a[0].upper()+a[1:],fruits))
print(new_list)

#2
fruits=["apple", "banana", "avocado", "apricot", "berry"]
new_list=list(map(lambda a:a.capitalize(),fruits))
print(new_list)


#Write a Python program to filter out words from a list that have more than 5 letters using lambda and filter().
fruits=["apple", "banana", "avocado", "apricot", "berry"]
fruit_list=list(filter(lambda a:len(a)<=5,fruits))
print(fruit_list)


#Write a Python program using a lambda function to remove duplicates from a list of numbers and sort the result in ascending order.
fruits=["apple", "banana", "avocado", "apple", "berry","avocado"]
fruit_set=set(fruits)




