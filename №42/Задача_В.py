print("Введите пять целых чисел:")
a,b,c,d,e=map(int,input().split())
max=a
if max<b:
    max=b
if max<c:
    max=c
if max<d:
    max=d
if max<e:
    max=e   
print("Максимальное число",max)
