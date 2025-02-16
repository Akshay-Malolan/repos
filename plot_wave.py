import numpy as np
import matplotlib.pyplot as plt

# Get inputs
k = float(input("Enter wave number k: "))  
omega = float(input("Enter angular frequency omega: "))
A = float(input("Enter amplitude A: "))  

# Set x-axis scale based on k
x_min = 0 
x_max = 2*np.pi/k
x = np.linspace(x_min, x_max, 100) 
#Time scale 
t = np.linspace(0, 2*np.pi, 100)    

# Plot
fig, ax = plt.subplots()
ax.set_ylim(-2*A, 2*A)

for ti in t:
    ax.clear()  
    y = A * np.sin(k*x - omega*ti)
    ax.plot(x, y)
    ax.hlines(0, x_min, x_max, colors='k')   
    ax.vlines(0, -2*A, 2*A, colors='k')
    plt.pause(0.05)  
    
plt.show()