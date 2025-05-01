# 스택으로 append ( pop )을해서 닫히는지 검사
# 홀수개로 남으면 NO 짝수로 맞아떨어ㅈ면 YES
# s[0] = ( s[1] = ( s[2] = ) s[3] = ) s[4] = )
# 들어오는 괄호가 열린 괄호면 append
# 들어오는 괄호가 닫힌 괄호면 pop
# append(s[0])
# append(s[1])
# pop(s)
# pop(s)
# pop()을 못함 인덱스가 -1이 되니까 이러면 실패
T = int(input())
for i in range(0,T) :
    s = list(input())
    stack = []
    flag = 1
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append(s[i])
        elif s[i] == ')' and len(stack) > 0 :
            stack.pop()
        else :
            flag = 0
            break
    if flag and not stack : print("YES") # 비어있지 않으면 ( 얘가 남아있는걸수도 있다
    else : print("NO")

## 다른풀이
# https://wookcode.tistory.com/49
T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")



