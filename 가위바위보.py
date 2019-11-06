from random import randint
while(True):
    c=randint(1,3)
    print("1.가위 2.바위 3.보")
    a=int(input())
    if c==1:
        if a==1:
            print("비김")
        elif a==2:
            print("이김")
            break
        elif a==3:
            print("짐")
    if c==2:
        if a==1:
            print("짐")
        elif a==2:
            print("비김")
        elif a==3:
            print("이김")
            break
    if c==3:
        if a==1:
            print("이김")
            break
        elif a==2:
            print("짐")
        elif a==3:
            print("비김")