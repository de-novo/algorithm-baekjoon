a,b = map(int,input().split())


if(b>=45):
    b-=45
   
else:
    if(a==0):
        a=23
    else:
        a-=1
    
    b=b+60-45

  

print(a,b)
