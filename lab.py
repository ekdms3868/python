"""
1+2+3...+n=10000을 넘지 않는 가장 큰 값과 그때의 n값

sum=0
i=1
while(sum<10000):
    sum=sum+i
    i=i+1
print(i-1)
print(sum-i)
"""
"""
가위바위보

from random import *
while(True):
    c=randint(1,3)
    print("1:가위 2:바위 3:보")
    m=int(input())
    if c==1:
        if m==1:
            print("비김")
        if m==2:
            print("이김")
            break
        if m==3:
            print("짐")
    if c == 2:
        if m==1:
            print("짐")
        if m==2:
            print("비김")
        if m==3:
            print("이김")
            break
    if c == 3:
        if m==1:
            print("이김")
            break
        if m==2:
            print("짐")
        if m==3:
            print("비김")
"""
"""
1에서 100까지 1씩 증가하며 반복하고, 홀수의 합을 구해라

sum=0
for i in range(1,101):
    if i%2 !=0:
        sum=sum+i
print(sum)
"""
"""
2단부터 9단까지 구구단을 출력하라

for a in range(2,10):
    for b in range(1,10):
        print("%dx%d=%d"%(a,b,a*b))
"""
"""
별 출력
*
**
***
"""
a=int(input())

for i in range(1,a+1):
    for k in range(1,i+1):
        print("*", end="")
    print("")