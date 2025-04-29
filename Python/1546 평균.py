n = int(input())
score = list(map(int, input().split()))
maxScore = max(score)

for i in range(n):
    score[i] = score[i]/maxScore*100

print(sum(score)/n)