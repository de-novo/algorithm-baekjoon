import sys
# N, K = map(int, sys.stdin.readline().split())



# n = int(sys.stdin.readline())
# val = [list(sys.stdin.readline().split()) for _ in range(n)]

# for i in val:
#     print( int(i[0])+int(i[1]))



# import sys

# n = int(sys.stdin.readline())
# n_list = [sum(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]

# print(*n_list, sep='\n')

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)