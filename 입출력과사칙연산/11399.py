# def minimalTime (length,time):
# 
# # times = input().split()


length = int(input(''))
times = list(int(x) for x in input('').split())


times.sort()



def minimalTimes(length,timesList):
    sum = 0
    length = length
    for x in timesList:
        sum += length*x
        length -=1

    return sum;

solution = minimalTimes(length,times)

print(solution)