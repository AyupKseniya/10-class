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
def y(i, l):
    t = i * l
    while i!= 0 and l!= 0:
        if i>l:
            i%=l
        else:
            l%=i
    return t // (i + l)
print("НОД(",a,",",b,")","=",k(a,b))
print("НОК(",a,",",b,")","=",y(a,b))

