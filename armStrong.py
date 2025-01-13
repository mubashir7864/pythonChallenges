'''a program to check Armstrong number'''

#153: 13+53+33=153



nu ='153'

def armstrong(nu):
    sum=0
    leng=len(nu)
    for i in nu:
        sum += int(i)**leng
    if sum == int(nu):
        print("its a Armstrong Number")
    else:
        print("its not  armstrong number")

armstrong("153")
armstrong("47")
armstrong("1")
