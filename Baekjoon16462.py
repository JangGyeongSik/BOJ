import sys
N=int(sys.stdin.readline())
grades=[]
for i in range(N):
    grade=sys.stdin.readline()
    grade=grade.replace('0', '9')
    grade=grade.replace('6', '9')
    grade_num = int(grade)
    if  grade_num >= 100:
        grade_num = 100
    grades.append(grade_num)
print(round(sum(grades) / N))
