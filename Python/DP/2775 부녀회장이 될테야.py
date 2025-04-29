# # DP 알고리즘
# # 1. DP로 풀 수 있는 문제인지 확인한다
# # 2. 문제의 변수 파악
# # 3. 변수 간 관계식 만들기(점화식)
# # 4. 메모하기
# # 5. 기저 상태 파악하기
# # 6. 구현하기

#     1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 0   1 2 3 4 5 6 7 8 9 10 11 12 13 14
# 1   1 3 6 10 15
# 2   1 4 10 20
# 3   1 5 15 35
# 4   1 6 21 56
# 5

# 2차원 배열에 x,y 인덱스로 값을 저장하면 될듯..?
# ab = (a-1)(1) + (a-1)(2) + ... + (a-1)(b)
# 1층 3호 = 0층1호 + 0층2호 + 0층 3호
# 1층 4호 = 1층 3호 + 0층4호

# arr[x][y] = arr[x-1][y] + arr[x][y-1] (x>0 y>0)


#### 잘못된 코드
# arr=[[]]
# arr[0]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# T = int(input())
# target = [[]]
# for i in range(0,T) :
#     target[i][0] = int(input())
#     target[i][1] = int(input())

# for t in range(0,T) :
#     for i in range(1,target[t][0]+1) : # 행
#         for j in range(0, target[t][1]): # 열
#             if( j == 0 ) : arr[i][j] = arr[i-1][j] + 0
#             else : arr[i][j] = arr[i-1][j] + arr[i][j-1]

# for i in range(0,T) :
#     print(arr[target[i][0]][target[i][1]]


#### gpt가 수정한 코드
T= int(input())
target = []
for _ in range(T) :
    k = int(input())
    n = int(input())
    target.append((k,n))

arr = [[0]*15 for _ in range(15)]
for i in range(15):
    arr[0][i] = i+1

for i in range(1,15) :
    for j in range(15) :
        if j == 0 : arr[i][j] = arr[i-1][j]
        else :
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

for k,n in target :
    print(arr[k][n-1])

#### 다른 풀이
# 내가 생각한 방법은 1~14호 까지 0층을 모두 값을 할당한 후
# 전 층의 같은 호와 같은 층의 이전호의 합을 계산하려고 했음

# 아래 풀이는 그냥.. 0층을 내가 구하고자 하는 호까지만 값을 주고
# 원하는 층,호 까지 계속 누적하면 결국 마지막값이 인원수가 됨

# people = [1,2,3,4]
# for문 한 번 돌렸을 때 : people = [1+0=1,2(자기자신)+1(이전꺼)=3,3(자기자신)+3(이전꺼)=6,4(자기자신)+6(이전꺼)=10]
# for문 두 번 돌렸을 때 : people = [1+0=1,3+1=4,6+4=10,10+10=20]


T = int(input())

for i in range(T) :
    k = int(input())
    n = int(input())
    people = [ i for i in range(1,n+1) ] # 0층 초기화, 호는 구하고자 하는 곳까지만

    for x in range(k) : # 층
        for y in range(n) : # 호
            if y == 0: continue
            people[y] += people[y-1] 
    print(people[-1]) # 맨 마지막이 구하고자 하는 층호의 인원수

    

