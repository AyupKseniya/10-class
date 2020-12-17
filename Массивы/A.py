from random import randint
print("Массив: ")
a=[randint(0,100)for i in range(5)]
print(a)
n=int(5)
s=sum(a)/n
print("Среднее арифметическое",s)
