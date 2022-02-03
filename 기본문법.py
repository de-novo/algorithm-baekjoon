###입력 받는법들

#정수입력
length = int(input(''))

#여러게 입력받아서 리스트화
times = list(int(x) for x in input('').split())
times.sort()

#튜플
a =tuple(int(x) for x in input().split())


x, y = input().split() 


import sys
N, K = map(int, sys.stdin.readline().split())
a,b = map(int, input().split())

### format string
name = input()
print("{}!!?".format(name))




### for idx,val in list
b = list(input())
for index,value in enumerate(b):
    len(b)
    print(index)



### list method
''.join()
b.reverse()