import sys
n = int(sys.stdin.readline())
test = 1
while test < n:
    test *= 2
if test == n:
    print(1)
else:
    print(0)
