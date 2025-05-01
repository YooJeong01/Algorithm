# 얘도 0 나오면 pop하고 아니면 append 해서
# 맨마지막에 숫자로 조인해서 출력하면 될듯?

# ValueError: invalid literal for int() with base 10: ''
# 이 에러는 int() 함수가 빈 문자열'' 을 숫자로 바꾸려해서 실패했다는 의미다..

K = int(input())
number = []
for _ in range(K) :
    n = int(input())
    if n == 0 :
        number.pop()
    else :
        number.append(n)
print(sum(number))