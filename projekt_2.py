import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, projection='3d')

z_lim = 40
number = 50000
n = np.arange(0, number, 1)


def label(equation):
   label = 'O' + str(equation)
   return label


def ratio(objekt):
   eqs = list(objekt.values())[0]
   ratio = eqs[0]/eqs[1]
   return ratio

# list is [Classical, Quantum]
algorithms = [
              {"Shor's Algorithm": [(np.exp(np.log(n) ** (1/3) * (np.log(np.log(n))) ** (2/3)) ** (1/3)), (np.log(n) ** 3)]},
              {"Testing Group Commutivity": [(n), (n**(2/3) * np.log(n))]},
              {"Element Distinctions": [(n), (n**(2/3))]},
              {"Matrix Product Verification": [(n**2), (n**(5/3))]},
              {"Grover's Algorithm": [(n), (np.sqrt(n))]},
              {"Triangle in Graph": [(n**2), (n**1.25)]},
              {"Quantum Fourier Transformation": [(np.log(n) * n), (np.log(n))]}  
              ]
algorithms.reverse()

counter = 1
for algorithm in algorithms:
   ax.scatter(xs=n,
              ys=counter,
              zs=ratio(algorithm),
              label=list(algorithm.keys())[0])
   counter += 1

ax.set_yticks(np.arange(1, len(algorithms) + 1)) 
ax.set_zlim([0, z_lim])
ax.set_xlim([0, number])
ax.set_xlabel('n (number of inputs)')
ax.set_ylabel('Algorithms')
ax.set_zlabel('Complexity Ratio (c/r)')
plt.title('Comparison of Quantum and Classical Complexity')
plt.legend()
plt.show()
