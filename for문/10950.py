# times = list(int(x) for x in input('').split())

num = int(input())
val = [list(input().split()) for _ in range(num)]

print(val)


for i in val:
    print(int(i[0])+int(i[1]))