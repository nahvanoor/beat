#for
l1=[2,4,6,8,9]
l2=[1,3,4,6,9]
l3=[]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
l3


#while
l1=[2,4,6,8,9]
l2=[1,3,4,6,9]
l3=[]
i=0
while i<len(l1):
    j=0
    while j<len(l2):
        if l1[i]==l2[j]:
            l3.append(l1[i])
        j+=1
    i+=1
l3


#function
l1=[2,4,6,8,9]
l2=[1,3,4,6,9]
def common(l1,l2):
    l3=[]
    i=0
    while i<len(l1):
        j=0
        while j<len(l2):
            if l1[i]==l2[j]:
                l3.append(l1[i])
            j+=1
        i+=1
    return l3
common([2,4,6,8,9],[1,3,4,6,9])

