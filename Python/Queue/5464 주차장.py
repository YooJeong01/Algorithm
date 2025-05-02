# https://www.acmicpc.net/problem/5464
# N : 주차 공간의 수
# M : 주차장을 이용하는 차량의 수
# 주차는 선입선출! 여러개 비었으면 인덱스 작은순서대로 이용
from collections import deque

N, M = map(int, input().split())
price = []
# 주차장 공간별 단위 무게당 요금을 저장한 배열
for _ in range(N) :
    price.append(int(input()))
#print(price)

car = []
# 주차장을 이용하는 차량 별 무게
for _ in range(M) :
    car.append(int(input()))
#print(car)

wait = []
# 문제에서 제시한 주차장 현 상황 (+ 들어옴, - 나감)
for _ in range(M*2) :
    wait.append(int(input()))
#print(wait)

answer = 0 # 총 수입


#waiting = []
waiting2 = deque([])

park = [0]*(N) # 주차하는 상황을 저장할 배열
for i in range(M*2) :

    if wait[i] > 0 : # 들어오는 차인 경우
        if 0 in park : # 주차장 자리가 있는 경우
            # park.index(0)으로 if문  통과여부를 정했는데
            # 이렇게 되면 0번째 인덱스가 반환될경우 항상 else로 예외처리 된다
            # 오름차순으로 주차
            parkIndex = park.index(0)
            #print(parkIndex)
            park[parkIndex] = wait[i]

        else : # 주차장 자리가 없는 경우
            #waiting.append(wait[i]) # 웨이팅 리스트에 등록
            waiting2.append(wait[i])
        #print("park : ",park)
        #print("waiting : ",waiting)

    elif wait[i] < 0 : # 나가는 차인경우
        # 나가는 차 번호
        carIndex = abs(wait[i])
        parkIndex = park.index(carIndex)
        # 요금계산
        answer += price[parkIndex]*car[carIndex-1]
        # 주차장 비우기
        park[parkIndex] = 0
        # 만약 웨이팅이 있다면
        # if waiting :
        #     # 웨이팅 첫번째 차를 해당 빈 구역에 넣어주기
        #     park[parkIndex] = waiting.pop(0)
        if waiting2 :
            park[parkIndex] = waiting2.popleft()

print(answer)


