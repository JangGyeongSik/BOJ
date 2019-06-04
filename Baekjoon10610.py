import sys
num= sorted([int(i) for (i) in sys.stdin.readline().rstrip()], reverse=True)

if num[len(num)-1] or sum(num) %3 != 0:
    print("-1")
    
else:
    for i in num:
        print(i, end="")
