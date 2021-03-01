from random import *
n,m=4,4
a= [[randint(0,255) for j in range(m)] for i in range(n)]
for i in range(n):            
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = " ")
    print()
    
summ=0
for i in range(n):
    for j in range(m):
        summ += a[i][j]
        sred_yark= summ/(n*m)      
print("Средняя яркость",sred_yark)
print("Результат:")
for i in range(n):
    for j in range(m):
        if a[i][j]<sred_yark:
            a[i][j]=0
        else:
            a[i][j]=255
for i in range(n):
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = " ")
    print()

