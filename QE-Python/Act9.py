l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 =[]

for i in l1:
    if i %2 !=0:
        l3.append(i)
print(l3)
for i in l2:
    if (i %2==0):
        l3.append(i)
print(l3)

        
