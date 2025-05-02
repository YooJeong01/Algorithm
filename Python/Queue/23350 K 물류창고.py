# # https://www.acmicpc.net/problem/23350
# # 우선 순위가 낮은 순서대로 적재
# # 우선 순위가 같은 경우 무거운 순서대로 적재
# # 우선 순위에서 밀리면 레일(대기)로 보냄 -> 비용발생
# # 우선 순위가 같은데 이미 가벼운게 실린경우? 가벼운거 빼내고 무거운거 넣음
# # (규칙맞을때까지 반복)
# # 빼낸거 모아놓은 곳은 순서 상관없음 그냥 다시 넣을때 무게순대로 넣어주면 됨 (FIFO X)
# # 비용 발생 : 적재할때, 빼낼때
# # N : 컨테이너 수
# # M : 우선순위 종류
# #
# # 2 + 1 + 2 + 1 + 3 + 2 + 1
#
# # 튜플로 (우선순위, 무게) 순차대로 저장
#
# N, M = map(int, input().split())
# box = []
# for _ in range(N) :
#     rank, weight = map(int, input().split())
#     box.append((rank, weight))
#
#
# rail = [] # 레일(빼낼거 담을곳)
# space = [] # 적재공간
# money = 0
# i=0
# r=0
# flag = 0
# while len(space) < N :
#     if len(space) > 0 : # 하나라도 담겨있을때
#         if space[-1][0] < box[i][0] : # 우선순위 값이 큰 경우
#             if flag :
#                 while len(rail) > 0 :
#                     space.append(rail[r])
#                     r += 1
#                     money += 1
#             else :
#                 space.append(box[i]) # 적재
#                 i = (i + 1) % M
#                 money += 1
#
#         elif space[-1][0] == box[i][0] and space[-1][1] >= box[i][1] :
#             # 우선순위 값이 같고
#             # 무게가 이전꺼보다 같거나 작을때
#             space.append(box[i]) # 적재
#             i = (i + 1) % M
#             money += 1
#         # 우선순위 값이 작거나, 우선순위는 같지만 무게가 무거운 경우 (빼내는 케이스)
#         else :
#             rail.append(space.pop())
#             money += 1
#             flag = 1
#             rail.sort()
#     else : # 적재된게 아무것도 없는 경우
#         space.append(box[i])
#         i = (i + 1) % M
#         money += 1
# print(money)
