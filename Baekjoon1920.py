import sys
N=sys.stdin.readline()
num=set(map(int, sys.stdin.readline().split()))
M=sys.stdin.readline()
for i in map(int, sys.stdin.readline().split()):
    if i in num:
        print('1')
    else:
        print('0')
