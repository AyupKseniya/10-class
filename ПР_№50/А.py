c,v=map(int,input("Введите два натуральных числа: ").split())
def Nod(a,b):
    if a==0 or b==0:
        return a+b
    if a>b:
        return Nod(a-b,b)
    else:
        return Nod(a, b-a)
print("НОД (",c,",",v,")=",Nod(c,v))  
