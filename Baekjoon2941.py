import sys
cl = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = sys.stdin.readline().rstrip()
for i in range(len(cl)):
    a = a.replace(cl[i],str(i))
print(len(a))
