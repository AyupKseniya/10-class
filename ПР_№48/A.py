def sum(a):
    s=0
    while a!=0:
        s+=a%10
        a=a//10
    return s

n=int(input("Введите натуральное число: "))
print("Сумма цифр числа",n,"равна",sum(n))
