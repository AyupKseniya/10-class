'''
9.42
sl=input("Введите слово")
print(sl[::-1])
'''
'''
9.44
sl = input("введите слово")
t = sl[::-1]
print(t)
'''
'''
9.46
n=("_")
print(n*8)
'''
'''
9.48
sl=input("введите слово")
print("+"*4,sl,5*"_")
'''       
'''
9.54
s=input()
buc="мин"
k=0
for i in s:
    if i in buc:
        k+=1
print(k)        
'''
'''
9.68
s=input()
sumvol="+-"
k=0
for i in s:
    if i in sumvol:
        k+=1
print(k)
'''
'''
9.70
s=input()
glas="уеыаоэяию"
k=0
for i in s:
    if i in glas:
        k+=1
print(k)  
'''
'''
9.52
s = input("введите предложение").split()
c = input("")
for i in range(len(s)):
    if c in s[i]:
        print(s[i])
'''
'''
9.56
s=input("Введите предложение")
n=s.count("нн")
print(n)
'''
'''
9.172
s = input("введите предложение").split()
a=0
for i in range(len(s)):
    if len(s[i])>a:
        a=len(s[i])
        s1=s[i]
print(s1)
'''
'''
9.60
sl=input("введите предложение")
k=0
n=(" ")
for i in sl:
    if i in n:
        k+=1
print(k)        
'''
'''
9.62
sl=input("введите предложение")
d=sl.count("а")
d=d/len(sl)*100
print(int(d))
'''
