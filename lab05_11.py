"""
두 점의 x,y 좌표를 입력 받아서 직선의 기울기, y절편, x절편을 출력하라
입력 예)
x1:2
y1:4
x2:6
y2:-2
출력 예)
직선의 기울기:
y절편:
x절편:
"""
from line import*
x1=int(input("x1:"))
x2=int(input("x2:"))
y1=int(input("y1:"))
y2=int(input("y2:"))

print("직선의 기울기",slope(x1,x2,y1,y2))
print("y절편",y_intercept(x1,x2,y1,y2))
print("x절편",x_intercept(x1,x2,y1,y2))
