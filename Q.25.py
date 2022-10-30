a=[4,6,4,3,3,4,3,4,3,8]
b=[]
count=0
k=int(input("enter"))
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
            j+=1
            if count>k:
                b.append(a[i])
                print(b)
            i+=1





            

