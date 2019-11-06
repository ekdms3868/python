"""
두 정수를 입력받아, 두 정수의 약수를 모두 출력하라
만약 1이외의 다른 공약수가 없는 경우에는, "공약수: 없습니다."를 출력하라.
입력 예)
첫번째 수:15
두번째 수:45
출력 예)
공약수:3

a=int(input("첫번째 수:"))
b=int(input("두번째 수:"))
max=max(a,b)
min=min(a,b)
g=1
for i in range(2,max+1):
    c=max%i
    d=min%i
    if c==0 and d==0:
        g=i
        print(i,end=" ")
print("최대 공약수:",g)
if g==1:
    print("공약수: 없습니다.")
"""
"""
두 정수를 입력받아, 두 정수의 약수를 모두 출력하라
만약 1이외의 다른 공약수가 없는 경우에는, "공약수: 없습니다."를 출력하라.
입력 예)
첫번째 수:15
두번째 수:45
출력 예)
공약수:3
"""
a=int(input("첫번째 수:"))
b=int(input("두번째 수:"))
c=0
if a>b:
    t=a
    a=b
    b=t

for i in range(2,a+1):
    if a%i==0 and b%i==0:
        c=c+1
print("공약수:", c)
if c == 0:
    print("공약수: 없습니다.")