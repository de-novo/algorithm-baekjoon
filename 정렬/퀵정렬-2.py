from operator import le
import time
import sys
sys.setrecursionlimit(10**9)

start = time.time()  # 시작 시간 저장x
 
L = list(range(10000))[::-1]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(L))


print("time :", time.time() - start)  

