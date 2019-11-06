"""
두 수를 입력받아, 절대값이 큰 수으이 절대값, 절대값이 작은 수의 절대값을 출력하라
"""
x=int(input("첫번째 수:"))
y=int(input("두번째 수"))

print(max(abs(x),abs(y)))
print(min(abs(x),abs(y)))