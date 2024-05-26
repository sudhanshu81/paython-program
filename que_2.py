#//wap to find the greatest of 3 numbers entered by the user.
a=int(input("enter num1:"))
b=int(input("enter the num2:"))
c=int(input("enter the num3:"))
if(a>=b and a>=c):
    print("grestest number:",a)
elif( b>=c):
    print("greatest number is:",b)
else:
    print(" greatest number is:",c)