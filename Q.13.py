a=[1,1,2,3,4,4,5,6,1]
i=0
count=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
            d=count,a[i]
            b.append(d)
        c.append(b)
        j+=1
        i+=1
print(c)
    