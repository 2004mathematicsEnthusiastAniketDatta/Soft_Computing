import matplotlib.pyplot as plt
import numpy as np
import skfuzzy
x=np.arange(20)
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
mf=skfuzzy.gbellmf(x,a,b,c)
plt.plot(x,mf)
plt.show()
x=float(input("Enter the element:"))
norm=1/(1+abs((x-c)/a)**(2*b))
print("Membership value: ",mf)
