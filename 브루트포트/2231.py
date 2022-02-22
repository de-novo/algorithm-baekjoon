# # 분해합 다국어
# # 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# # 2 초	192 MB	75949	34849	27583	45.894%
# # 문제
# # 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# # 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# # 입력
# # 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# # 출력
# # 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.


# # def sol(N):
# #     L=[1]
# #     while 1:
# #         if L[-1]<=N:
# #             ''.split(L[-1])
    
# # print(list(map(int,list('123'))))


# # 100x+10y+z +x+y+z = N
# # 101x+11y+2z = N
# # 1001x+101y+11z+2j=N
# # # L=[1,2,3]
# # 12345
# # 12360
# # 12372




# def sol(N):
#     for i in range(1,N+1):
#         L = list(map(int,list(str(i))))
#         s = i + sum(L)
        
#         if N==s:
#             return i
#         if i==N:
#             return 0
    
# print(sol(int(input())))





def sol(N):
    leng =len(str(N))
    Start = N-leng*9 if N > leng*9 else 1 ;
    for i in range(Start,N+1):
        L = list(map(int,list(str(i))))
        s = i + sum(L)
        if N==s:
            return i
        if N==i:
            return 0


N = int(input())
print(sol(N))


