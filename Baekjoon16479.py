#16479 컵라면측정하기
#컵라면 높이** 알아내기 
#https://www.acmicpc.net/user/kqkdn

K = int(input())
a, b= map(int, input().split())
print(K**2-((b-a)/2)**2)
