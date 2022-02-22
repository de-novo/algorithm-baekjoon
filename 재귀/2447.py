# 별 찍기 - 10
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	44703	23432	17374	52.398%
# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

# 입력
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

# # 
# def star(N):
#     list=[['*']*N]*N
#     for i,v in enumerate(list):
#         if i%3==1:
#             for i2,v2 in enumerate(v):
                
#                 if i2%3==1:
#                     list[i][i2]=True
                    
#                 else :
#                     print(i, i2)
#                     list[i][i2]='*'  

#     return list


# def star(n):
#     list=[]
#     for i in range(n):
#         line = []
#         for x in range(n):
#             if (i%3==1 & x %3==1) or (i//3== & x//3==2):
#                 line.append(' ')
#             else :
#                 line.append('*')
#         list.append(line)
#     return list               
            

# for i in star(27):
#     print(i)


 
def star(n):
    
    if n==1:
        return ['*']
    L=star(n//3)
    
    S=[]
    for i in L: 
        S.append(i*3)
    for i in L :
        S.append(i+' '*(n//3)+i)
    for i in L: 
        S.append(i*3)
    # print(S)
    return S



print('\n'.join(star(int(input()))))



