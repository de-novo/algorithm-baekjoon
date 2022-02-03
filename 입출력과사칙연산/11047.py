
x, y = input().split() 
x=int(x)
y=int(y)
coinList = []

for i in range(0,x):
    coinList.append(int(input()))



def minimalCoin(price,coinList):
    coinList.sort(reverse=True)
    price = price
    coinNum = 0
    for i in coinList:
        if price//i!=0:
            coinNum+=price//i
            price-=price//i*i
    return coinNum


soultion = minimalCoin(y,coinList)

print(soultion)
