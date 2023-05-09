l=[]
for i in range(1,101):
    l.append(i)
    
l1=[]
l2=[]
for i in l:
    cubes=0
    cubes = i**3
    if cubes%4==0 or cubes%5==0:
        l1.append(i)
        l2.append(cubes)

print(l1)
print(l2)
