print("Введите координаты точки А:")
x1,y1=map(float,input().split())
print("Введите координаты точки B:")
x2,y2=map(float,input().split())
from math import*
a=sqrt((x2-x1)**2+(y2-y1)**2)
print("Длина отрезка АВ=",a)

