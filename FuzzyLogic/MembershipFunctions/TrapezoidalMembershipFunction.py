import matplotlib.pyplot as plt
import numpy as np

a=int(input("Enter the leftmost point:"))
b=int(input("Enter the rightmost point:"))
m=int(input("Enter the peak value 1:"))
n=int(input("Enter the peak value 2:"))
x=(a,m,n,b)
y=(0,1,1,0)
for u,v in zip(x,y):
    plt.text(u,v,f"({u},{v})")
plt.plot(x,y,marker='o')
plt.title("Trapezoidal Membership Function")
plt.grid()
plt.show()

def trapezoidalMembershipFunction(x):
    if x <= a or x >= b :
        mem=0
    elif a < x <= m:
        mem=(x-a)/(m-a)
    elif m <= x <= n:
        mem=1
    elif n <= x < b:
        mem=(b-x)/(b-n)
    else:
        mem=0
    print("Membership value is: ",mem)

trapezoidalMembershipFunction(7)


