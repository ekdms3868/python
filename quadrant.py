"""
좌표를 입력받아서 좌표가 속하는 사분면을 화면에 출력하는 프로그램을 작성하라
x축, y축, 원점에 있는 경우도 있다.
입력 예)
x좌표:3
y좌표:5
좌표(3,5)는 1사분면에 있습니다.
"""
x=int(input("x좌표:"))
y=int(input("y좌표:"))
if x>0:
    if y>0:
        print("좌표 (%d,%d)는 1사분면에 있습니다."%(x,y))
    if y<0:
        print("좌표 (%d,%d)는 4사분면에 있습니다." % (x, y))
    if y==0:
        print("좌표 (%d,%d)는 y축에 있습니다." % (x, y))
if x<0:
    if y>0:
        print("좌표 (%d,%d)는 2사분면에 있습니다." % (x, y))
    if y<0:
        print("좌표 (%d,%d)는 3사분면에 있습니다." % (x, y))
    if y == 0:
        print("좌표 (%d,%d)는 x축에 있습니다." % (x, y))
if x==0:
    if y==0:
        print("좌표 (%d,%d)는 원점에 있습니다." % (x, y))
    else:
        print("좌표 (%d,%d)는 y축에 있습니다." % (x, y))