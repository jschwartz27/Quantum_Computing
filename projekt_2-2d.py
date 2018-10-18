from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

number = 1**9
n = np.arange(0, number, 1000)
fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111)


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
              {"Grover's Algorithm": [(n), (np.sqrt(n))]},
              {"Element Distinctions": [(n), (n**(2/3))]},
              {"Triangle in Graph": [(n**2), (n**1.25)]},
              {"Matrix Product Verification": [(n**2), (n**(5/3))]},
              {"Testing Group Commutivity": [(n), (n**(2/3) * np.log(n))]}
              ]

ax.set_xscale("log")
ax.set_yscale('log')

ax.set_xlim([100, number])
for algorithm in algorithms:
   ax.scatter(
              x=n,
              y=ratio(algorithm),
              label=list(algorithm.keys())[0]
              )
ax.set_xlabel('n (number of inputs)')
ax.set_ylabel('Ratio of Complexity (c/r)')
plt.title('Comparison of Quantum and Classical Complexity')
plt.legend()
plt.show()
