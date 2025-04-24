import numpy as np 
import matplotlib as plt


a=float((input("Enter the left most point:")))
b=float(input("Enter the right most point:"))

m=float(input("Enter the peak Value:"))

x=(a,m,b)
y=(0,1,0)
for u,v in zip(x,y):
    plt.text(u,v)
    

