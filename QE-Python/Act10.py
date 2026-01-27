l = tuple(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if(l[i]%5==0):
        l1.append(l[i])
print(l1)