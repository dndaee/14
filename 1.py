%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 500) 

y = np.sqrt(x) * np.sin(10 * x)

plt.figure(figsize=(10, 6)) 
plt.plot(x, y, linestyle='-', color='darkblue', linewidth=2, label=r'$Y(x) = \sqrt{x} \cdot \sin(10x)$')

plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)

plt.title("Графік функції Y(x) = √x · sin(10x)", fontsize=14)

plt.legend(loc='upper right')

plt.grid(True)

plt.show()
