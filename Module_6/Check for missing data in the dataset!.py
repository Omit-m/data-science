# import pandas as pd
# import numpy as np
#
# data_dic = {
#     'M': [1, 2, np.nan, 4, np.nan],
#     'N': [11, 12, 13, 14, 15],
#     'O': [np.nan, np.nan, np.nan, np.nan, np.nan],
#     'P': [16, np.nan, 18, 19, 20]
# }
#
# df = pd.DataFrame(data_dic)  # Creating a DataFrame
# nan_df = df.isna()  # DataFrame showing True for NaN values, False otherwise
# print(nan_df)



import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'A': [21, np.nan, 22, 4, np.nan],
    'B': [31, 32, 33, 34, 35],
    'C': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'D': [46, 47, np.nan, 48, 49]
}

df = pd.DataFrame(data)

# Count NaN values in the DataFrame
def count_nan_values(dataframe):
    return dataframe.isna().sum().sum()  # Total count of NaN values

nan_count = count_nan_values(df)
print(f"Number of NaN values in the DataFrame: {nan_count}")

# Filling NaN values using different methods
# Forward fill
df_ffill = df.ffill()

# Backward fill
df_bfill = df.bfill()

# '0' fill
df_zero_fill = df.fillna(0)

# Displaying the results
print("\nDataFrame after forward fill:")
print(df_ffill)

print("\nDataFrame after backward fill:")
print(df_bfill)

print("\nDataFrame after '0' fill:")
print(df_zero_fill)

print("Original DataFrame:")
print(df)
