

 #  하나의 리스트 생성

 # 정렬할 데이터 7 5 9 0 3 1 7 2 9 1 4 8 0 5 2


#  인덱스 => 값 == 개수

# L = [7,5,9,0,3,1,7,2,9,1,4,8,0,5,2]
import time
start = time.time()  # 시작 시간 저장
 

L = list(range(10000))[::-1]
count = [0] * (max(L)+1)


for i in range(len(L)):
    count[L[i]] += 1 

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end =' ')

print("time :", time.time() - start)  

