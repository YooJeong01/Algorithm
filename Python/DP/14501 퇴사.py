# 점화식을 세우자
# 관계성 파악!
# 하루당 단가..?
# t[1] t[4] t[5]
# t[1] t[4] 
# t[2], t[3], t[4], t[5]
# t[3] t[4] t[5]
# t[4] t[5]

# 상담기간이 남은 기간보다 길어도 안됨
# t[i]  i일에 상담을 잡았을때 남은 기간은 n=n-i
# 그다음 상담의 제일 빠른건 t[n-i]
# t[n-i][1] <=n-i 조건 만족시 상담 가능
# 상담될때 append 해줘야할듯 (1,4,5)이런식
# 그래서 그때 p값을 다 더해서 max를 구해야할듯?

# (X)
# N = int(input())
# t = []
# for _ in range(N) :
## a, b = int(input().split())
## int()는 하나의 값만 변환이 가능하다 그래서 에러나는 행
#     a, b = map(int,input().split())
#     t.append((a,b))
## [0]으로 N 길이의 t를 만들고선 append를 하면 [0,0,,,,(a,b)]이렇게 되는 꼴이다
## 만약 [0]초기화 해둘거면 t[i] = (a,b) 이런식으로 사용해야한다
# 빈리스트 하나 만들고 append 해서 길이 늘려가는게 효율적임(인덱스 바로 접근할 필요없을때)


# arr = [0]*240


# def func1(i,n,temp=[]) :
#     for i in range(N):
#         if t[i][0] <= n : # 상담기간이 남은기간보다 적다면
#             temp.append(i) # 가능하니까 temp에 상담일자 넣어주고
#             n = n - t[i][0] # 남은 기간은 방급 넣어준 상담일자의 소요시간을 뺀 기간 
#         if n == 0 :
#             arr.append(temp) # 남은 기간이 0이 되면 그간 쌓아둔 인덱스를 정답 배열에 넣기
#             return 0
#         else :
#             func1(i+t[i][0],n,temp) # 다음 인덱스가 될 번호, 남은 기간


# for k in range(N):
#     n = N
#     temp = [0]*N
#     func1(k,N,temp)


# maxTotal = 0
# for j in range(len(arr)) :  
#     total = 0
#     for m in range(len(arr[j])) :
#         idx = arr[j][m]
#         total += t[idx][1]
#     maxTotal = max(total,maxTotal)

#----------------------------------------------------------------

# gpt가 고쳐준 재귀코드
N = int(input())
t = []
for _ in range(N):
    a, b = map(int, input().split())  # 입력 받기 수정
    t.append((a, b))                  # (상담 기간, 금액)

results = []  # 가능한 상담 조합 인덱스를 저장할 리스트

def func1(i, day, temp=None):
    if temp is None:
        temp = []
    
    if i >= N:  # 날짜를 초과한 경우는 종료
        results.append(temp[:])  # 복사해서 저장
        return
    
    # 현재 상담을 하는 경우
    if i + t[i][0] <= day:
        temp.append(i)
        func1(i + t[i][0], day, temp)
        temp.pop()  # 백트래킹

    # 현재 상담을 하지 않는 경우
    func1(i + 1, day, temp)

# 탐색 시작
func1(0, N)

# 수익 계산
maxTotal = 0
for schedule in results:
    total = 0
    for idx in schedule:
        total += t[idx][1]  # 금액 합산
    maxTotal = max(maxTotal, total)

print(maxTotal)


#### 다른 풀이(dp를 역순으로)

n =int(input())
days = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    if i + days[i][0] <= n:
        dp[i] = max(days[i][1] + dp[i+days[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])

#### 다른풀이 2
N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

def solve(i):
    if i>=N:
        return 0
    ret = 0
    if i+timeTable[i][0]<=N :
        ret = solve(i+timeTable[i][0])+timeTable[i][1]
    ret = max(ret,solve(i+1))
    return ret

print(solve(0))
