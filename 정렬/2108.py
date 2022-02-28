import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

print(round(sum(li)/n))

li.sort()
print(li[n//2])

cnt=Counter(li).most_common()
print(cnt[1][0] if len(cnt)>1 and cnt[0][1]==cnt[1][1] else cnt[0][0])

print(max(li)-min(li))

