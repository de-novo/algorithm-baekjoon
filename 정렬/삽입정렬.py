import time
start = time.time()  # 시작 시간 저장
 

# L=list(range(10000))[::-1]
L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]

for i in range(1,len(L)):
    for z in range(i,0,-1):
        if L[z] < L[z-1] :
            L[z], L[z-1] = L[z-1], L[z]
        else : 
            break

print(L)


print("time :", time.time() - start)  


# 시간복잡도 O(n^2)

# L=list(range(10000))[::-1]
# time : 16.98903203010559

# L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]
# time : 5.507469177246094e-05