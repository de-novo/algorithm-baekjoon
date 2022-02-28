from operator import le
import time
import sys
sys.setrecursionlimit(10**9)

start = time.time()  # 시작 시간 저장
 


# L = list(range(10000))[::-1]
L= [2,3,4,5,6,1,2,2,2,3,4,5,7,8,9,0]


def quick_sort(array, start, end):
    # print('play')
    if start >= end:
        return ;

    pivot = start # 피봇은 첫 번째 원소
    left = start + 1
    right = end

    while(left <= right):
        #피벗보다 큰 데이터 찾을때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left +=1

        #피봇보다 작은 데이터 찾을때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -=1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]

        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end) 


quick_sort(L,0,len(L)-1)
print(L)





print("time :", time.time() - start)  




