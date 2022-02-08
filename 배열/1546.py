N = int(input())
L = list(int(x) for x in input().split())


M = max(L)

result=sum(list(map(lambda x : x/M*100 ,L)))/N
print(result)