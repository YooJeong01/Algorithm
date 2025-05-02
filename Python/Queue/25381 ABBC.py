# # https://www.acmicpc.net/problem/25381

# # 무조건 A-B or B-C 순서로 지울수있음
# # 서로 떨어져있어도 상관없음 순서만 지키면 됨
# # 큐 FIFO
# # 큐는 양방향인건가?
#
# # ABCBA인경우
# # 1. 문자열 입력받기
# # 2. 모든 문자에 대해 탐색하는데
# # 3. A인 경우 그 뒷 차례중 B가 나오면
# # 4. 해당 인덱스 pop하거나 0처리?
# # 5. B인 경우 그 뒷 차례중 C가 나오면
# # 6. 해당 인덱스 pop하거나 0처리?
# # 7. 문자열 끝날때까지 시행하고 해당 시행횟수 저장하기
# # 8. 시행횟수중 가장 큰 수 출력
#
# s= input()
#
# def search(char,start_idx,string) :
#     for i in range(start_idx, len(s)) :
#         if string[i] == char :
#             return i
#
# cnt = 0
# for i in range (0,len(s)) :
#     if s[i] == 'A' :
#         b_idx = search('B', i+1, s)
#         if b_idx :
#             s[i] = 'X'
#             s[b_idx] = 'X'
#             cnt += 1
#     elif s[i] == 'B' :
#         c_idx = search('C', i+1, s)
#         if c_idx :
#             s[i] = 'X'
#             s[b_idx] = 'X'
#             cnt += 1
#
# # for문을 두개 돌려야 하나?
# # a-bcba
# # b-cba
# # c-ba
#
# for i in range(0,len(s)) :
#     if s[i] == 'A' :
#         for j in range(i+1, len(s)) :
#             if s[j] == 'B' :
#                 s[i] = 'X'
#                 s[j] = 'X'
#                 cnt += 1
#     if s[i] == 'B' :
#         for j in range(i+1, len(s)) :
#             if s[j] == 'C' :
#                 s[i] = 'X'
#                 s[j] = 'X'
#                 cnt += 1
#

## 다른풀이
# 쌍을 만들때 모두 B가 쓰이기 때문에 이 문제의 키는 B의 갯수보다 쌍의 갯수가 클수없다
# 따라서 쌍을 만들수 있는 경우에 대해서 ans를 공유해서 누적한다
# 만약 이게 원본의 B의 개수보다 많은 경우에는 최대 B의 갯수까지만 답이 되고,
# ans이 작은 경우에는 ans이 답이 된다

S = list(input())
N = len(S)
ans = 0
cntA = 0
cntB = 0
cntTotalB = 0

for i in range(N) :
    if S[i] == 'A' :
        cntA += 1
    elif S[i] == 'B' and cntA :
        cntA -= 1
        ans += 1

for i in range(N) :
    if S[i] == 'B' :
        cntB += 1
        cntTotalB += 1
    elif S[i] =='C' and cntB :
        cntB -= 1
        ans += 1

print( min(ans, cntTotalB) )















