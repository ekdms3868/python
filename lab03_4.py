"""
사용자로부터 연도를 입력받아서, 해당 연도가 며칠로 구성되어 있는지 출력하라.
4로 나뉘어 떨어지면 윤년이다. 단, 100으로 나뉘어 떨어지면 윤년이 아니며, 400으로 나뉘어 떨어지면 윤년이다.
입력 예)
연도: 2000
출력 예)
366일 입니다.

year=int(input("연도:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("366일 입니다.")
        else:
            print("365일 입니다.")
    else:
        print("366일 입니다.")
else:
    print("365일 입니다.")
"""



"""
사용자로부터 연도를 입력받아서, 해당 연도가 며칠로 구성되어 있는지 출력하라.
4로 나뉘어 떨어지면 윤년이다. 단, 100으로 나뉘어 떨어지면 윤년이 아니며, 400으로 나뉘어 떨어지면 윤년이다.
입력 예)
연도: 2000
출력 예)
366일 입니다.
"""
year=int(input("연도:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("366일 입니다.")
        else:
            print("365일 입니다.")
    else:
        print("366일 입니다.")
else:
    print("365일 입니다.")