n=int(input("Enter number: "))
m=n+n
a=[]
for i in range(1,m):
    if i % 2 !=0:
        a.append(i)    
    if len(a)>=n:
        break
print(a)