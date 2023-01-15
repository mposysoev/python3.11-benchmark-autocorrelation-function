from matplotlib import pyplot as plt
import numpy as np
import sys

input_file = sys.argv[1]

data = np.loadtxt(input_file)

plt.plot(data[:, 0], label="X component")
plt.plot(data[:, 1], label="Y component")
plt.plot(data[:, 2], label="Z component")
plt.legend()
plt.show()
