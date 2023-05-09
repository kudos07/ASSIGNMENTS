#a for llop is used when you know the n times the loop is going to execute and vice versa for while

for i in range(1,10):
    print(i)
    
i=1
n=int(input("how many times this should be executed"))
while(i<=n):
    print(i)
    i=i+1