"""
이율, 기간, 원금을 입력받아서 원리급 합계를 출력하라
입력 예)
연이율:0.03
기간(년):2
원금(원):1000000
출력 예)
원리금:1060900
"""
a=float(input("연이율:"))
b=int(input("기간(년):"))
c=int(input("원금(년):"))
print("원리금:",int(c*(1+a)**b))