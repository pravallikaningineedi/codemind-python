l,r,k=map(int,input().split())
i=l
c=0
while i<=r:
    if i%k==0:
        c+=1
    i+=1
print(c)