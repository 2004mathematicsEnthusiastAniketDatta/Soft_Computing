import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

# Get parameters from user
a = float(input("Enter a (slope): "))
b = float(input("Enter b (center): "))

# Generate universe variable
x = np.arange(0, 20, 0.1)

# Generate sigmoid membership function
sig = fuzz.sigmf(x, b, a)  # Note: in fuzz.sigmf, the order is (x, c, a) where c is center and a is slope

# Plot the membership function
plt.figure(figsize=(8, 5))
plt.plot(x, sig, 'b', linewidth=1.5, label='Sigmoid MF')
plt.title('Sigmoid Membership Function')
plt.xlabel('Universe Variable')
plt.ylabel('Membership Value')
plt.grid(True)
plt.legend()
plt.show()

# Calculate membership value for a specific element
x_val = float(input("Enter the element: "))
mem = fuzz.sigmf(np.array([x_val]), b, a)[0]
print(f"Membership value: {mem}")
