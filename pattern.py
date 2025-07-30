for i in range(1,6):
    print(i*"*")
    
for i in range(7,0,-1):
    print(i*"*")
    
x=7    
for i in range(x):
    print((x-i)*" ",i*"*")
    
for i in range(x):
    print((x-i)*" "+i*"* ")
    
for i in range(x,0,-1):
    print((x-i)*" "+i*"* ")
    

for i in range(x):
    print((x-i)*" ",i*" *") 
    
for row in range(1,7):
    for col in range(0,row):
        print("*",end="")
    print("")
    
for row in range(1,6):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print(row,end=" ")
    print()
    
for row in range(7,0,-1):
    for col in range(8,row,-1):
        print(row,end=" ")
    print()
    
for row in range(6,0,-1):
    for col in range(row,7):
        print(col,end=" ")
    print()
    
str="python"
for row in range(1,7):
    for col in range(0,row):
        print(str[col],end=" ")
    print()
print(str[5])
    
for row in range(5,0,-1):
    for col in range(1,row):
        print(col,end=" ")
    print()
    
string="python"
for row in range(6,0,-1):
    for col in range(0,row):
        print(string[col],end=" ")
    print()   

for row in range(1,7):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()
    
num=1
for row in range(6):
    for col in range(row):
        print(num,end=" ")
        num=num+1
    print()
    
num=1
for row in range(6):
    for col in range(row):
        print(num,end=" ")
        num=num+1
    print()
    num=1
    
num=1
for row in range(6):
    start=num+row-1
    for col in range(row):
        print(start,end=" ")
        start=start-1
        num=num+1
    print()
    
num=2    
for row in range(1,6):
    num=row+1
    for col in range(row):
        print(row,end=" ")
    for i in range(row+1,6):
        print(num,end=" ")
        num=num+1
    print()
    
    
    
    
    

    
    
