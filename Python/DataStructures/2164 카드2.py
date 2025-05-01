# 1. pop(0)
# 2. append(pop(0))

card = []
N = int(input())
for i in range(1,N+1) :
    card.append(i)

while(len(card)>1) :
    card.pop(0)
    card.append(card.pop(0))
print(card[0])

# 123     3->2
# 23
# 32
# 2
#
# 1234    4->4
# 234
# 342
# 42
# 24
# 4
#
# 12345   5->2
# 2345
# 3452
# 452
# 524
# 24
# 42
# 2
#
# 123456 6->4
# 23456
# 34562
# 4562
# 5624
# 624
# 246
# 46
# 64
# 4
#
# 1234567 7 ->6
# 234567
# 345672
# 45672
# 56724
# 6724
# 7246
# 246
# 462
# 62
# 26
# 6
#
# 12345678 8->8
# 2345678
# 3456782
# 456782
# 567824
# 67824
# 78246
# 8246
# 2468
# 468
# 684
# 84
# 48
# 8
#
# 123456789

# 1(1)
# 2(2)

# 3(2)
# 4(4)

# 5(2)
# 6(4)
# 7(6)
# 8(8)

# 9(2)
# 10(4)
# 11(6)
# 12(8)
# 13(10)
# 14(12)
# 15(14)
# 16(16) 2^4

# 2- 4- 8- 16
# 17(2) 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32(2^5)
# 시간초과나서 규칙 찾아보니
# 2^N 폭으로 늘어나면서 마지막으로 남게 됨
# 주어진 N(갯수)가 2의 제곱수라면 답은
# 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192

# 틀린 코드
# N이 2의 거듭제곱수인 경우에는 수식을 계산하면 0이 나오기 때문에
# 자기 자신이 답인데 다르게 나옴 그래서 틀림
N = int(input())
power = 1
while power*2 <= N :
    power *= 2
if N == 1 : print(1)
elif N == 2 : print(2)
else : print((N-power)*2)

# gpt가 고쳐준 코드
N = int(input())
power = 1
while power * 2 <= N:
    power *= 2

if N == power:
    print(N)
else:
    print((N - power) * 2)



# 다른 풀이
# https://velog.io/@error_io/%EB%B0%B1%EC%A4%80-2164-%EC%B9%B4%EB%93%9C2-Python
import math
N = int(input())
square = 2 ** math.floor(math.log2(N))
answer = (N-square) * 2
if answer == 0 : print(N) # ex. 4, 8, 16, 32 ,,,
else : print(answer) # ex. 15, 17, 23 ,,,


# 다른 풀이 (deque 사용)
import collections
card_num = int(input())
card_deque = collections.deque([i for i in range(1, card_num +1)])

while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[0])