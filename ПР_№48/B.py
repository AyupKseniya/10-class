a,b=map(int,input("Введите два натуральных числа: ").split())
def k(n,m):
    while n!=m:
        if m>n:
            c=m-n
        else:
            c=n-m
        n=m
        m=c
    return c
print("НОД(",a,",",b,")","=",k(a,b))  
