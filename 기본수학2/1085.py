import sys

x,y,w,h = map(int,sys.stdin.readline().split())


wHalf = w/2
hHalf = h/2 

xD=0
yD=0

if x>wHalf:
    xD= w-x
else : 
    xD= x


if y>hHalf:
    yD= h-y
else : 
    yD= y
    
print(xD if xD<yD else yD)



### 최적화

x,y,w,h = map(int,sys.stdin.readline().split())

m = min([x,w-x,y,h-y])
print(m)