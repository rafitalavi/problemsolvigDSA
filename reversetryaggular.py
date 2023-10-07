t = int(input())
for x in range(t):
    for y in range(0,t-x-1):
        print(" ",end="")
   
    for y in range(2*x+1):
        print("*",end="")
    

    print()     
for x in range(t,0 ,-1):
    for y in range(t-x):
        print(" ",end="")
   
    for y in range(2*x-1):
        print("*",end="")
    

    print() 

