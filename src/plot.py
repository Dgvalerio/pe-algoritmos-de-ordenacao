import matplotlib.pyplot as plt
import numpy as np

# random
# 10k 50k 100k
quantity = ['10k', '50k', '100k']
order = ['random', 'descending', 'ascending']

random_bubble = [3.8430888750000003, 97.429318958, 388.89946075]
random_heap = [0.029721041000000004, 0.1806922499999999, 0.38613158300000805]
random_insertion = [1.7693349170000001, 44.580948457999995, 177.66800154100002]
random_merge = [0.023134083, 0.11069920799999977, 0.23884987499999966]

# descending
# 10k 50k 100k
descending_bubble = [5.319059000000038, 133.6917888339999, 539.628022417]
descending_heap = [0.027305582999929356, 0.17142008300004363, 0.3666278329999386]
descending_insertion = [3.557775541999945, 89.09632425000007, 356.67007549999994]
descending_merge = [0.015887292000002162, 0.0908361670000204, 0.1934168340000042]

# ascending
# 10k 50k 100k
ascending_bubble = [0.0004604999999173742, 0.002335000000130094, 0.004665208000005805]
ascending_heap = [0.030934082999920065, 0.1906232500000442, 0.39953191699987656]
ascending_insertion = [0.0008448329999737325, 0.004346707999957289, 0.008627375000060056]
ascending_merge = [0.015495417000011003, 0.0887757089999468, 0.18938420900008168]

fig, axs = plt.subplots()
axs.plot(random_bubble, quantity, color='yellow')
axs.plot(random_heap, quantity, color='red')
axs.plot(random_insertion, quantity, color='blue', linestyle='--')
axs.plot(random_merge, quantity, color='green', linestyle='--')

plt.show()
