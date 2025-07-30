words=['me','the','that','for','this','is','my']
two=[]
three=[]
four=[]
for i in words:
    if len(i)==2:
        two.append(i)
    elif len(i)==3:
        three.append(i)
    else:
        four.append(i)
        
        
print(two)
print(three)
print(four)
        