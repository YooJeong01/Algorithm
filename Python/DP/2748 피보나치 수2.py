
# ans2 = ans1 + ans0 => 1 + 0 = 1
# ans3 = ans2 + ans1 => 1 + 1 = 2
# ans4 = ans3 + ans2 => 2 + 1 = 3
# 내가 푼 방식은 DP의 상향식 접근 방법
n = int(input())

ans = [0]*(n+1)
ans[1] = 1

if(n>=2) :
    for i in range(2,n+1) :
        ans[i] = ans[i-1] + ans[i-2]
print(ans[-1])

# 다른 풀이 (append 사용)
n = int(input())
dp = []
dp.append(0)
dp.append(1)

for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])
    
print(dp[n])

# 메모이제이션 방식 (재귀 호출)




