value=1
while value<6:
    print(value)
    value+=1
    
    
value=5
while value>0:
    print(value)
    value-=1
    flowers=['rose','lilly','tulip','jasmine']

    
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
    
    
num=[]
value=int(input("enter a number"))
while value!=0:
    num.append(value)
    value=int(input("enter a number"))
num
    
   
num=[]
sum=0
value=int(input("enter a number"))
while value!=0:
    if sum+value>100:
        break
    num.append(value)
    sum=sum+value
    value=int(input("enter a number"))
print(sum)   
num
    


num=[5,3,6,0,8,3,0,2,0]
num1=num.copy()
value=0
while value<len(num):
    if num[value]==0:
        num1.remove(num[value])
        num1.append(num[value])
    value+=1
num1
    

