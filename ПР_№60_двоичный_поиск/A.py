from random import*
s=[]
s=[randint(-10,10)for i in range(9)]
print("масив",s)

for i in range(9-1):
    for j in range(9-2,i-1,-1):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
print("после сортировки",s)            

x=int(input("введите число "))
ch=0
for i in range(9):
      if s[i]==x:
          ch+=1
print("число",x,"найдено")
print("количество сравнений",ch)
