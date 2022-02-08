###입력 받는법들

#정수입력
length = int(input(''))

#여러게 입력받아서 리스트화
times = list(int(x) for x in input('').split())
times.sort()
val = [int(input()) for _ in range(n)][::-1] #뒤집기
val = [list(input().split()) for _ in range(num)]

# 1 2 3 4 5 6 
L = list(int(x) for x in input().split())
numbers = list(map(int, input().split()))

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
min(list)
max(list)
L.index()
# lambda x : < 익명함수
list(filter(lambda x : int(x)<y,val))
[x for x in val if vali(x)]

from functools import reduce
reduce(lambda x,y : x*y ,L)

# 예외처리
Try:
  [...]
except:
  [...] 


import math
#반올림
round()
#내림
math.floor() 
#올림 
math.ceil()

#소수점 자리수 표기 f-string
print(f'{num:.0f}')