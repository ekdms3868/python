"""
5!=5*4*3*2*1=120

a=int(input("양의 정수:"))
sum=1
for i in range(a,1,-1):
    sum=i*sum
    print(i,end="*")
"""
a=int(input("양의 정수:"))
f=1
i=1

for x in range(a,0,-1):
    if x==1:
        print(x,end="=")
    else:
        print(x,end="*")

while i<=a:
    f=f*i
    i=i+1

print(f)