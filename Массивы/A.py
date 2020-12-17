from random import randint
print("Массив: ")
a=[randint(0,100)for i in range(5)]
print(a)
s=sum(a)/len(a)
print("Среднее арифметическое",s)
