"""
두점의 x좌표, y좌표를 매개 변수로 받아서, 기울기를 반환하는 slope()함수,
y 절편을 반환하는 y_intercept 함수
x 절편을 반환하는 x_intercept 함수
를 포함하는 line.py 파일을 정의한다.
"""
def slope(x1,x2,y1,y2):
    a=float(y2-y1)/float(x2-x1)
    return a

def y_intercept(x1,x2,y1,y2):
    return y1-slope(x1,x2,y1,y2)*x1
def x_intercept(x1,x2,y1,y2):
    return y_intercept(x1,x2,y1,y2)/(slope(x1,x2,y1,y2)*-1)