"""
x좌표와 y좌표를 입력 받아, 원점으로부터의 거리를 출력하라.
입력 예)
x좌표:3
y좌표:-6
출력 예)
원점으로부터의 거리:6.708
"""
from math import*

x=int(input("x좌표:"))
y=int(input("y좌표:"))
c=sqrt(x**2+y**2)
print(c)