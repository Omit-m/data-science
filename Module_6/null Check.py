import pandas as pd
import numpy as np

data_dic = {
    'M': [1, 2, np.nan, 4, np.nan],
    'N': [11, 12, 13, 14, 15],
    'O': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'P': [16, np.nan, 18, 19, 20]

}
df = pd.DataFrame(data_dic)
A= df.isnull().sum().sum()

print(A)