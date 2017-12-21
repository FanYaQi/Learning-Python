import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
  result = 1 / (1 + np.exp(-x))
  return result

x = np.arange(-10,10,0.1)
y = 2*np.sin(x)

plt.plot(x,y)

plt.grid(color='g', linestyle='dashed', linewidth=0.3)
plt.xlabel('variable x')
plt.ylabel('sigmoid')

plt.title('First Graph for Little Angel', y=1.02)

plt.show()
