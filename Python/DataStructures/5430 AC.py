## reverse를 들어올떄마다 바로바로 하게되면 시간초과 난다
## deqeue로 해도 마찬가지다

from collections import deque

#popleft() rotate()

T = int(input())
for _ in range(T):
    plist = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n == 0 :
        print("error")
        continue

    flag = 1
    for p in plist :
        if p == 'R' :
            if len(arr) == 0 :
                flag = 0
                break
            arr.reverse()
        elif p == 'D' :
            if len(arr) == 0 :
                flag = 0
                break
            arr.popleft()
    if flag :
        print("["+",".join(arr)+"]")
    else : print("error")


### 다른 풀이
# https://clap0107.tistory.com/16
from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = input()[1:-1]
    nums = x.split(',') if n > 0 else []

    queue = deque(nums)

    reverse = 0
    flag = False

    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            reverse += 1
        else:
            if len(queue) == 0:
                print('error')
                flag = True
                break
            elif reverse % 2 == 1:
                queue.pop()
            else:
                queue.popleft()

    if not flag:
        result = list(queue)
        if reverse % 2 == 1:
            result = reversed(result)
        print('[' + ','.join(result) + ']')


## gpt가 위 코드를 개선한 코드
from collections import deque
import sys

input = sys.stdin.readline  # ⭐ 빠른 입력 함수 사용 (많은 입력 처리 시 시간 단축)

t = int(input())

for _ in range(t):
    p = input().strip()             # 명령어 문자열
    n = int(input())                # 배열 크기
    x = input().strip()[1:-1]       # [1,2,3] 형태의 문자열 → 1,2,3만 추출

    # 빈 배열이 아니면 , 기준으로 나눔
    nums = x.split(',') if x else []

    queue = deque(nums)            # O(1) pop/popleft 가능한 deque 사용
    reverse = False                # R 명령이 홀수번이면 True
    error = False                  # 에러 발생 여부

    for cmd in p:
        if cmd == 'R':
            reverse = not reverse  # R이 나올 때마다 뒤집을지 말지만 토글
        elif cmd == 'D':
            if not queue:
                print('error')
                error = True
                break
            if reverse:
                queue.pop()        # 뒤집힌 상태면 뒤에서 삭제
            else:
                queue.popleft()    # 앞에서 삭제

    if not error:
        # 출력 시에만 reversed 사용 → O(N)
        result = list(reversed(queue)) if reverse else list(queue)
        print('[' + ','.join(result) + ']')
