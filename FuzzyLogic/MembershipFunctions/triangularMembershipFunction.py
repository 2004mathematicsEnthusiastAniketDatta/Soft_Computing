import numpy as np 
import matplotlib.pyplot as plt


a=float((input("Enter the left most point:")))
b=float(input("Enter the right most point:"))

m=float(input("Enter the peak Value:"))

x=(a,m,b)
y=(0,1,0)
for u,v in zip(x,y):
    plt.text(u,v,f"({u},{v})")
plt.plot(x,y,marker='o')
plt.title("Triangular Membership Function")
plt.grid(False)
plt.show()


def triangularMembershipFunction(x):
    if x <= a or x >= b:
          mem=0
    elif a < x <= m:
          mem=(x-a)/(m-a)
    elif m <= x < b:
          mem= (b-x)/(b-m)
    else: 
            mem=0
    print("Membership value is: ",mem)

triangularMembershipFunction(4)
    