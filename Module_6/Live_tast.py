
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [21, np.nan, 22, 4, np.nan],
    'B': [31, 32, 33, 34, 35],
    'C': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'D': [46, 47, np.nan, 48, 49]
}


df = pd.DataFrame(data)
print(df) # print dataframe
def count_nan_values(dataframe):
    return dataframe.isnull().sum().sum()
nan_count = count_nan_values(df)
print(f"Number of NaN values in the DataFrame: {nan_count}")


# Clean the NaN values using Forward fill
df_ffill1 = df.fillna(method='ffill')
print("DataFrame after forward fill:")
print(df_ffill1)


# Clean NaN values using backward fill
df_bfill2 = df.fillna(method='bfill')
print("DataFrame after backward fill:")
print(df_bfill2)



# Clean NaN values using '0' fill
df_zero_fill = df.fillna(0)
print("DataFrame after '0' fill:")
print(df_zero_fill)
