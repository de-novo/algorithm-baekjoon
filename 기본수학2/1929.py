# 소수 구하기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	147983	41506	29294	26.788%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
from math import sqrt
a,b = map(int,input().split())


for i in range(a,b+1):
    r = int(sqrt(i))
    X = True
    for x in range(2,r+1):
        if i%x==0:
            X =False
            break
    if X and i!=1:    
        print(i)