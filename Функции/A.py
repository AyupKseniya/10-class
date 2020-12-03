print("введите три натуральных числа:")
q,w,e=map(int,input().split())
def k(a,b,c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return (a,b,c)
print(k(q,w,e))
