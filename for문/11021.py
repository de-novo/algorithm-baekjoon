import sys
t = int(sys.stdin.readline())

for _ in range(t):
    
    a,b = map(int, sys.stdin.readline().split())
    print('Case #{}: {}'.format(_+1,a+b))