### sorting 정렬 .

데이터를 특정한 기준에 따라 순서대로 나열하는 것.
문제에따라 적절한 정렬 알고리즘이 공식처럼 사용됨

# 정렬 알고리즘 종류

1. 선택 정렬
    - 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복.
    - 시간 복잡도 O(n^2)
        - N + (N-1) + (N-2) + ..... + 2
            - (N^2 + N -2) / 2
            - > O(N^2)

```

L=[0,5,4,3,2,1]
for i in range(len(L)):
    min_index= i
    for z in range(i+1,len(L)):
        if L[min_index]>L[z]:
            min_index = z
    L[i], L[min_index] = L[min_index], L[i] #swap

print(L)


# L=list(range(10000))[::-1]
# time : 6.37929105758667

# L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]
# time : 5.698204040527344e-05
```

2. 삽입 정렬
    - 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입.
    - 선택정렬에 비해 구현 난이도는 높음. but , 일반적으로 더 효율적
    - 시간복잡도 O(n^2) , 반복문이 두 번 중첩되어 사용.
        - 데이터가 거의 정렬되어 있는 상태라면 매우 빠르다. -최선의 경우 O(N)

```
L = [0,5,4,3,2,1,8]

for i in range(1,len(L)):
    for z in range(i,0,-1):
        if L[z] < L[z-1] :
            L[z], L[z-1] = L[z-1], L[z]
        else :
            break

print(L)

# L=list(range(10000))[::-1]
# time : 16.98903203010559

# L=[4,12,3,4,5,6,7,8,9,0,98,5,4,3,2,4,3,5,6,8,9]
# time : 5.507469177246094e-05
```

3. 퀵 정렬

    - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬.
    - 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.
    - 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘.
    - 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정함.

    - 시간복잡도

        - 평균 O(NlogN) : 거의 절반씩 분할 한다면,
        - 최악 O(N^2)

    - 재귀적으로 수행됨.

```
]

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



# L = list(range(10000))[::-1]
# time : 2.864866018295288

# L= [2,3,4,5,6,1,2,2,2,3,4,5,7,8,9,0]
# time : 6.413459777832031e-05

```

```
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

```

3. 계수 정렬
    - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
        - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
    - 데이터의 개수가 N, 데이터(양수) 중 최대값이 K 일때 최학의 경우에도 수행 시간 O(N+K)를 보장
    - 0 과 9999999 단 두가지만 있다하면 비효율적.
    - 동일한 값을 가지는 데이터가 여러개 등장 할때 효과적
    - 성적, ( 랭킹?? )

```
L = list(range(10000))[::-1]
count = [0] * (max(L)+1)


for i in range(len(L)):
    count[L[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end =' ')
```


4. 힙 정렬
    - 힙 트리 구조를 이용하는 구조. 힙구조를 만드는 시간복잡도 O(N)
    - 이진트리 사용
    - O(NlogN)