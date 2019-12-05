import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(0,99,100)
y = np.zeros(len(n))
for i in n:
    i = int(i)
    x = i
    while x>=10:
        x = x-10
    z = ((x**2)-7)
    z = int(z)
    y[i] = z
plt.stem(n,y)