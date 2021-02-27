from random import *

n = int(input("введите количество строк в списке: "))
m = int(input("введите количество стобцов в списке: "))
a= [[randint(10,99) for j in range(m)] for i in range(n)]


for i in range(n):          
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = " ")
    print()

max_item =10
min_item=98
for i in range(n):
    for j in range(m):
        if a[i][j]> max_item:
            max_item = a[i][j]
for i in range(n):
    for j in range(m):
        if a[i][j]< min_item:
            min_item = a[i][j]
print("Максимальный элемент",(max_item))
print("Минимальный элемент",min_item)
