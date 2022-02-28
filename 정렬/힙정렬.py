
L = [5,2,3,9,6,1,8,4,7,11,23,44,56,1,0,2,3,4]
def heapify(array):
    for i in range(1,len(array)):
        c = i
        while c != 0 : 
            
            root = (c- 1)//2
            if array[root] < array[c]:
                array[root], array[c] = array[c], array[root]
            c = root
      
    return array


def heap_sort(array):
    S=[0]*len(array)
    
    for i in range(len(array)-1,-1,-1): 
        array = heapify(array[:i+1])
        S[i]=array[0]
        array[0], array[i] = array[i] ,array[0]
        # array = heapify(array[:i])
             

    return S


for i in heap_sort(L):
    print(i)


