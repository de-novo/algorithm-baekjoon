# 소수 찾기
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	101118	47824	38669	47.624%
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.


from math import sqrt


N = int(input()) 

A = list(map(int,input().split()))



def is_prime(n):
    R = int(sqrt(n)+1)
    if n == 1 :
        return False
    for i in range(2,R):

        if n %i == 0: 
            return False
        
    return True
    


print(list(map(is_prime,A)).count(True))


