''' Fibonacci series for first 12 numbers.'''
# 0 1 1 
a,b,c = 0,1,0

for i in range(12):
    print(a,end=",") # 0,1,1,2,3,5...........
    c=a+b # 0+1=1,1+1=2,1+2=3,2+3=5,...........
    a=b 
    b=c 

    


