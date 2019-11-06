"""
문제: 정수의 각 자리수의 합을 출력하라
입력 예)
정수:546
출력 예)
자리수의 합: 15
"""
a=int(input("정수:"))
b=0
while a>0:
    c=a%10
    b=b+c
    a=a//10
print("자리수의 합:%d" %b)

a=int(input("정수:"))
sum=0
while a>0:
    b=a%10
    a=a//10
    sum=sum+b
sum=sum+a
print(sum)