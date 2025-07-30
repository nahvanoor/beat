fruits=['apple','banana','grapes']
animals=('cat','dog','bear')
num1={1,4,5,7,8}
person={'name':'john','age':25}
dir(list)
fruits.append('orange')
fruit2=fruits.copy()
fruits.count('banana')
fruits.extend(['kiwi','mango'])
fruits.pop()
fruits.reverse()
fruits.remove('banana')
fruits.sort()
fruits.insert(2,'mango')
abc=[1,'banana','apple',4,6,9]


dir(tuple)
animals.count('cat')
animals.index('dog')

dir(set)
num1={1,4,5,7,8}
num1.add(6)
num2={2,3,6,9,4}
num1.difference(num2)
num2.difference(num1)
num2.difference_update(num1)
num1.intersection(num2)
num1.isdisjoint(num2)
num1.issubset(num2)
num1.issuperset(num2)
num1.pop()
num1.add(1)
num1.symmetric_difference(num2)
num1.union(num2)

dir(dict)
person={'name':'john','age':25}
person1=person.copy()
person.fromkeys('name')
person2=person
person.pop('age')
person1
person2



fruits=['apple','banana','grapes']
for value in fruits:
    value.upper()


for value in range(2,-1,-1):
    print(fruits[value])
    
for i in range(0,6):
    print("*"*i)
    
for i in range(1,6):
    print(" *"*i)
    
for i in range(7,0,-1):
    print("*"*i)
    

for row in range(1,6):
    for col in range(0,row):
        print("*",end="")
    print("")
    

for row in range(6,0,-1):
    for col in range(row,0,-1):
        print("*",end="")
    print("")   
    
for row in range(1,6):
    for col in range(0,row):
        print(" *",end="")
    print("")
    
    
for row in range(1,6):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end="")
    print("")

    
for row in range(6,0,-1):
    for space in range(7,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end="")
    print("")


for row in range(1,6):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(row):
     print()
    
for row in range(1,6):
    for col in range(1,row+1):
        if col==1 or col==row or row==5:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()
    

for row in range(1,6):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row+1):
        if col==1 or col==row or row==5:
            print(row ,end="")
        else:
            print("  ",end="")
    print()


for row in range(5,0,-1):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row+1):
        if col==1 or col==row or row==5:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    
    
    
#while
value=0
while value<6:
    print(value)
    value+=1
    
flowers=["lilly","rose","tulip","lotus"]
value=0
while value<len(flowers):
    print(flowers[value])
    value+=1
    
flowers=['rose','lilly','tulip','jasmine']   
value=len(flowers)-1
while value>=0:
    print(flowers[value])
    value-=1
    
row=0
while row<5:
    col=0
    while col<row:
        print("*",end=" ")
        col+=1
    print()
    row+=1

    
row=5
while row>0:
    col=row
    while col>0:
        print("*",end="")
        col-=1
    print()
    row-=1
    
    
    
row=0
while row<6:
    space=6
    while space>row:
        print(" ",end="")
        space-=1
    col=0
    while col<row:
        print("* ",end="")
        col+=1
    print()
    row+=1
    
    
row=5
while row>0:
    space=6
    while space>row:
        print(" ",end="")
        space-=1
    col=0
    while col<row:
        print("* ",end="")
        col+=1
    print()
    row-=1
    
    
list1=[46,79,24,35]
sum=0
for i in list1:
    sum=sum+i
print(sum)


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
        
