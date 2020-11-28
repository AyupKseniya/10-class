def k(a):
    b=0
    while a>0:
        b = b*10 + a%10
        a = a//10
    print("После переворота: ",b)    
n=int(input("Введите натуральное число: "))        
k(n)    
