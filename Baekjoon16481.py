#원 전문가 진우  16481
#평면에 있는 삼각형 ABC의 서로 다른 위치에 있는 세 방접원의 반지름의 길이가 r1, r2, r3일 때, 삼각형 ABC의 내접원의 반지름을 구하시오.
#Baekjoon/user/kqkdn
a, b, c= map(int, input().split())
print(1/(1/a+1/b+1/c))
