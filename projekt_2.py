from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, projection='3d')

z_lim = 40
number = 50000
n = np.arange(0, number, 1)
m = np.arange(0, 100, 1)
z = 2 * n
z2 = 4 * n

def label(equation):
   label = 'O' + str(equation)
   return label

def ratio(objekt):
   eqs = list(objekt.values())[0]
   ratio = eqs[0]/eqs[1]
   return ratio
a = n 

# list is [Classical, Quantum]
algorithms = [{"Shor's Algorithm": [(np.exp(np.log(a) ** (1/3) * (np.log(np.log(a))) ** (2/3)) ** (1/3)), (np.log(a) ** 3)]},
              {"Testing Group Commutivity": [(a), (a**(2/3) * np.log(a))]},
              {"Element Distinctions": [(a), (a**(2/3))]},
              {"Matrix Product Verification": [(a**2), (a**(5/3))]},
              {"Grover's Algorithm": [(a), (np.sqrt(a))]},
              {"Triangle in Graph": [(a**2), (a**1.25)]},
              {"Quantum Fourier Transformation": [(np.log(a) * a), (np.log(a))]}  
              ]
algorithms.reverse()
# Plot complexities

# t = np.arange(0.0, 6.0, 1)
# plt.yticks(range(0, len(t) + 1))

counter = 1
for algorithm in algorithms:
   ax.scatter(xs=n,
              ys=counter,
              zs=ratio(algorithm),
              label=list(algorithm.keys())[0])
   counter += 1

ax.set_yticks(np.arange(1, len(algorithms) + 1)) 
#ax.set_yticklabels([list(i.keys())[0] for i in algorithms])
ax.set_zlim([0, z_lim])
ax.set_xlim([0, number])
ax.set_xlabel('n (number of inputs)')
ax.set_ylabel('Algorithms')
ax.set_zlabel('Ratio of Complexity (c/r)')
plt.title('Comparison of Quantum and Classical Complexity')
plt.legend()
plt.legend()
plt.show()