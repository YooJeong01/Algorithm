# 시간 초과
# n = int(input())

# count = []
# def func1(n,cnt):
#     if(n==1) : 
#         count.append(cnt)
#         return cnt
#     if(n%3 ==0) :
#         func1(n/3, cnt+1)
#     if(n%2 ==0) :
#         func1(n/2, cnt+1)
#     func1(n-1,cnt+1)

# func1(n,0)
# print(min(count))


# 점화식 : dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)

n = int(input())
dp = [0]*10000001 # 0으로 초기화 시켜준다
# dp 에는 해당 숫자(index)를 만드는데 필요한 최소 연산 횟수가 저장된다

for i in range(2,n+1) :
    dp[i] = dp[i-1] + 1 # 연산 시행시마다 값을 +1 해준다

    if i%2==0 : 
        dp[i] = min(dp[i],dp[i//2]+1) 
        # 지금 시행횟수가 최소인지, 이전꺼에 +1한게 최소인지
    if i%3==0 :
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[n])


    