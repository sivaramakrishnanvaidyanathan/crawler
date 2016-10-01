__author__ = 'sivvaidyanathan'

import matplotlib.pyplot as plt, pandas as pd, numpy as np


df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                    'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

plt.figure();
df4.plot.hist(alpha=0.5)
plt.show();
