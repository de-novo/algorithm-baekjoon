# 네 번째 점 다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	27697	19958	18030	73.120%
# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.


# A = [list(map(int,(input().split()))) for _ in range(3)]

# yD = 0
# xD = 0

# for i,v in enumerate(A):
x=[]
y=[]   
X=0
Y=0
for i in range(3):
    S = list(map(int,input().split()))
 
    x.append(S[0])
    y.append(S[1])
for i in range(3):
    xc =x.count(x[i])
    yc =y.count(y[i])
    if xc==1:
        X= x[i]
    if yc==1 :
        Y = y[i]

print(X,Y)        