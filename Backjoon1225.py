#acmicpc.net/user/kqkdn1

import sys
a,b = map(str, sys.stdin.readline().rstrip().split(' '))

at = 0
bt = 0

for i in range(len(a)):
    at += int(a[i])
for j in range(len(b)):
    bt += int(b[j])

print(at*bt)

// a와b값을 받은후에 at,bt 연산자 지정
// 각 값을 배열에넣어준후 a의 append값과 b의 append값을 곱해준다.
// 문자열 오른쪽 개행문자를 제거하기위해 rstrip 사용 
