## reverse를 들어올떄마다 바로바로 하게되면 시간초과 난다
## deqeue로 해도 마찬가지다

from collections import deque

#popleft() rotate()

T = int(input())
for _ in range(T):
    plist = input()
    n = int(input())
    raw = input().rstrip()
    arr = deque(raw[1:-1].split(",") if n > 0 else [])
    # arr = deque(input().rstrip()[1:-1].split(","))
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
    nums = x.split(',')

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
        if reverse % 2 == 1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
