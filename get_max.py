"""
문제: 매개변수로 넘어온 리스트에서 최대값을 반환하는 get_max 함수를 정의한다.
프로그램에서,
l1=[3,5,-2,20,9] l2=[-4,374,3,1,4,7,-23] 을 정의한 후, 각각의 최대값을 출력하고, 두 최대값의 합을 출력하라
출력 예)
l1의 최대값:20
l2의 최대값:374
l1과 l2의 최대값의 합 = 394
"""
def get_max(l): #get_max 함수 정의
    max = l[0] #max를 리스트의 0번째 수로 저장
    for i in range(1,len(l)): #i가 1에서 list마지막까지
        if max<l[i]: #만약 max가 l[i]보다 작으면
            max=l[i] #max에 l[i] 저장
    return max #max 반환

l1=[3,5,-2,20,9] #l1 정의
print("list1의 최대값:",get_max(l1)) #l1의 최대값을 get_max 함수를 이용해 출력
l2=[-4,374,3,1,4,7,-23] #l2 정의
print("list2의 최대값:",get_max(l2)) #l2의 최대값을 get_max 함수를 이용해 출력

print("l1과 l2의 최대값의 합 =",get_max(l1)+get_max(l2)) #l1의 최댓값과 l2의 최댓값을 더해 출력