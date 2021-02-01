s=input("введите строку:")
s1=""
for c in s:
    if c=="а":
        c="б"
    elif c=="б":
        c="а"
    elif c=="Б":
        c="А"
    elif c=="А":
        c="Б"
    s1=s1+c
print(s1)
