import pandas as pd
import numpy as np

columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()

array_2d = np.arange(100, 0, -1).reshape(10, 10)

df = pd.DataFrame(array_2d, index=index, columns=columns)
# df[['c1', 'c2']]
df['new']= df['c1'] * df['c10']
df.drop('new',axis = 1, inplace = True)
subset = df[df['c1'] < 50]

print(df)
