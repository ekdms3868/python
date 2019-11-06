a=int(input("물건값을 입력하시오:"))
b=int(input("1000원 지폐개수:"))
c=int(input("500원 지폐개수:"))
d=int(input("100원 지폐개수:"))
e=a*1000+b*500+c*100-a

nc=e//500
e=e%500

nd=e//100
e=e%100

n1=e

print("500=",nc,"100=",nd,"1=",n1)