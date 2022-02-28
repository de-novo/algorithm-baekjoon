import time
start = time.time()  # 시작 시간 저장
 

# L=list(range(10000))[::-1]
L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]

for i in range(len(L)):
    min_index= i
    for z in range(i+1,len(L)):
        if L[min_index]>L[z]:
            min_index = z
    L[i], L[min_index] = L[min_index], L[i] #swap

print(L)

print("time :", time.time() - start)  




# 시간복잡도 O(n^2)

# L=list(range(10000))[::-1]
# time : 6.37929105758667

# L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]
# time : 5.698204040527344e-05