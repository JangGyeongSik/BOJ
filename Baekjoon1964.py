# 1964 오각형 
# https://www.acmicpc.net/user/kqkdn

import sys
n= int(sys.stdin.readline())
print(int((((3*n*n)+(5*n)+2)/2) % 45678))
