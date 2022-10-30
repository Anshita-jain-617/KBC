a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
count=0
i=0
b=[]
c=[]
while i<len(a):
    count+=1
    if count<=3:
        b.append(a[i])
    i+=3
c.append(b)
print(c)


    

    


