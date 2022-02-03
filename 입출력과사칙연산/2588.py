a = int(input())
b = list(input())



b.reverse()

for index,value in enumerate(b):
    print(int(value)*a)


b.reverse()
b=''.join(b)

print(a*int(b))
