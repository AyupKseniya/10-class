from random import randint
print("Массив: ")
a=[randint(0,100)for i in range(5)]
print(a)
s1=[i for i in a if i<50]
s2=[i for i in a if i>=50]
sr1=sum(s1)/len(s1)
sr2=sum(s2)/len(s2)
print("ср.арифм.элементов [0,50):",sr1)
print("ср.арифм.элементов [50,100]:",sr2)
