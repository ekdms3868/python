a=input("문자열을 입력하세요:")
b=len(a)//2
if len(a)%2!=0:
    print("중앙글자는",a[b])
else:
    print("중앙글자는",a[b-1],a[b])