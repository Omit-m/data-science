# import pandas as pd
# import numpy as np
#
# # Your DataFrame
# data_dic = {
#     'M': [1, 2, np.nan, 4, np.nan],
#     'N': [11, 12, 13, 14, 15],
#     'O': [np.nan, np.nan, np.nan, np.nan, np.nan],
#     'P': [16, np.nan, 18, 19, 20]
# }
#
# df = pd.DataFrame(data_dic)
#
# non_nan_count = df.count()
#
# print(non_nan_count)
#
# #
# # import pandas as pd
# # import numpy as np
# #
# # # Your DataFrame
# # data_dic = {
# #     'M': [1, 2, np.nan, 4, np.nan],
# #     'N': [11, 12, 13, 14, 15],
# #     'O': [np.nan, np.nan, np.nan, np.nan, np.nan],
# #     'P': [16, np.nan, 18, 19, 20]
# # }
# #
# # df = pd.DataFrame(data_dic)  # Creating a DataFrame
# #
# # # Filling null values in column 'M' with its mean
# # mean_M = df['M'].mean()  # Calculating mean of column 'M'
# # df['M'].fillna(mean_M, inplace=True)
# #
# # # Printing the column 'M' after filling null values with the mean
# # print(df['M'])
#
# import numpy as np
# import pandas as pd
#
# data_dic = {'M':[1,2,np.nan,4,np.nan],
#             'N':[11,12,13,14,15],
#             'O':[np.nan,np.nan,np.nan,np.nan,np.nan],
#             'P':[16,np.nan,18,19,20]}
# df = pd.DataFrame(data_dic)
#
# # Calculate the mean of column 'M'
# mean_M = df['M'].mean()
# print(mean_M)
import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, np.nan],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

X=df.fillna(0, inplace=True)
print(df)