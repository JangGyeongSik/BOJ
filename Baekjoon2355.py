# 2355 시그마.py
# https://acmicpc.net/user/kqkdn
a,b = map(int, sys.stdin.readline().split())
print(int((a+b)*(abs(a-b)+1)/2))
