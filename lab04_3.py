"""
사용자로부터 자연수를 입력받아서, factorial 값을 출력하라
입력 예)
자연수:3
출력 예)
3!=6
"""
a=int(input("자연수:"))
b=1
for i in range(a,0,-1):
    b=i*b
print("%d!=%d" %(a,b))
