import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




x = np.linspace(0, 10, 100)
y = np.random.rand(100)
sns.lineplot(x=x, y=y)
plt.show()
