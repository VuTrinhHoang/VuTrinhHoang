import math
n=int(input())
i=int(math.sqrt(n))
def prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return 0
    return 1
def check(n,i):  
    while n%i !=0:
        i-=1
    if(prime(i)==1):
        return i
    else :
        return check(n,i*i-1)
print(check(n,i))