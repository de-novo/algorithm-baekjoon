# 팩토리얼
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	98845	49997	41637	50.934%
# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.



# def fac(n):
#     s = 1 
#     if n == 0 :
#         return 1
#     for i in range(n):
#         s*=i+1
#     return s



# def fac(n,s):
   
#     if n == 0:
#         return s
#     else :
#         print(n)
#         s*=int(n)
#         return fac(n-1,s)   
# print(fac(int(input()),1))




def fac(n):
    
    if n == 0:
        return 1
    else :
        return n*fac(n-1)   
print(fac(int(input())))
