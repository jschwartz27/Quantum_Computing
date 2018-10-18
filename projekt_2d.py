from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111)

number = 1000000000
n = np.arange(0, number, 1000)
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

# tuple is (Classical, Quantum)
algorithms = [{"Quantum Fourier Transformation": [(np.log(n) * n), (np.log(n))]},
              {"Shor's Algorithm": [((2**np.log(n))**2), (np.log(n) ** 3)]},
              #{"Shor's Algorithm": [(np.exp(np.log(n)**(1/3) * (np.log(np.log(n)))**(2/3)) ** (1/3)), (np.log(n) ** 3)]},
              #{"Shor's Algorithm": [(np.exp(1.9*np.log(n)**(1/3) * (np.log(np.log(n)))**(2/3))), (((np.log(n))**2)*(np.log(np.log(n)))*(np.log(np.log(np.log(n)))))]},
              {"Grover's Algorithm": [(n), (np.sqrt(n))]},
              {"Element Distinctions": [(n), (n**(2/3))]},
              {"Triangle in Graph": [(n**2), (n**1.25)]},
              {"Matrix Product Verification": [(n**2), (n**(5/3))]},
              {"Testing Group Commutivity": [(n), (n**(2/3) * np.log(n))]}
              ]
# Plot complexities

ax.set_xscale("log")
ax.set_yscale('log')

#ax.set_xlim([2, number])
ax.set_xlim([100, number])
for algorithm in algorithms:
   ax.scatter(
              x=n,
              y=ratio(algorithm),
              label=list(algorithm.keys())[0]
              )
ax.set_xlabel('n (number of inputs)')
ax.set_ylabel('Ratio of Complexity (c/r)')
#ax.set_zlabel('Ratio of Complexity (c/r)')
plt.title('Comparison of Quantum and Classical Complexity')
plt.legend()
plt.show()
