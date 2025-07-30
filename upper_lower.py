string="Nahva@123"
upper=[]
lower=[]
number=[]
other=[]
for i in string:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isnumeric():
        number.append(i)
    else:
        other.append(i)
    
    
print(upper)
print(lower)
print(number)
print(other)