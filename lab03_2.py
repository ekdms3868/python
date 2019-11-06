print("주문 가능한 메뉴:")
menu_list=['햄버거','샌드위치','콜라','사이다']
print(menu_list)
a=int(input("메뉴번호(0-3):"))
b=int(input("개수:"))
print("선택된 메뉴:",menu_list[a])
if a==0:
    price=3000
elif a==1:
    price=2000
elif a==2:
    price=1000
elif a==3:
    price=1000

print("총가격:%d"%(price*b))
