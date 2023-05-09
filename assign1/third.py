n=int(input("enter units"))
mul=0
if n <=100:
    mul=n*4.5
elif n>100 and n<=200:
    mul=n*6
elif n>200 and n<=300:
    mul=n*10
elif n>300:
    mul=((100*4.5) + (100*6) + (100*10) +((n-300)*20))
    
print(mul)
