# Baekjoon 16134 조합 서브태스크 
# https://acmicpc.net/user/kqkdn
# 조합을 이용한 서브태스크 문제 

mod = 1000000007
f = lambda n, m:m < 1 or n * f(n-1, m-1)//m
print(f( *map( int, input().split() )) % mod)

