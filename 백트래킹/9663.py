# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 10 초	128 MB	59050	29448	19337	49.361%
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


# ######################################################################################### 

# N = int(input())


# B=[]
# for i in range(1,N+1):
#     for n in range(1,N+1):
#         B.append([i,n])

# L=[]
# S=0
# def solve(BoardList):
#     global S
#     # print(BoardList)
#     if len(L)==N:
#         S +=1
#         return
#     for i in range(1,N+1):
#         for n in range(1,N+1):
#             W=[i,n]
#             if  W in BoardList:
                    
#                     BoardList.remove(W)
#                     L.append(W)
#                     solve(dont(i,n,BoardList))
#                     L.pop()


# def dont(a,b,B):
#     for i in range(1,N+1):
#         Xp = a+i
#         Xm = a-i
#         Yp = b+i
#         Ym = b-i 
#         B = list(filter(lambda c : c!=[Xp,Yp] and c!=[Xp,Ym] and c!=[Xm,Yp] and c!=[Xm,Ym] and c!=[Xp,b] and c!=[Xm,b] and c!=[a,Yp] and c!=[a,Ym] ,B ))

#     return B

# solve(B)

# print(S)
# ################################
# #답은 나오나 시간초과 , 비효율적임  ## 효율적인 방법 == 1차원으로 생각.
# ################################
# ######################################################################################### 

# [index,value]

N = int(input())
L =[0]*N
T =[False]*N
num = 0 
print(L) #
def check(n):
    for i in range(n): 
        if L[n]==L[i] or abs( L[n]-L[i] )== n - i :
            return False    
    return True        


def solve(n):
    global num
    if n == N :
        num+=1
        return

    for i in range(N):
        if T[i] :
            continue

        L[n] = i 
        if check(n):
            T[i] = True
            solve(n+1)
            T[i] = False

solve(0)


print(num)

# =============================

import sys
input = sys.stdin.readline

n = int(input())
rows = [0] * n
visited = [False] * n
cnt = 0
def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]: 
            continue

        rows[x] = i
        if check(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False




dfs(0)
print(cnt)