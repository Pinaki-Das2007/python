"""
vertically (row-wise)
horizontally (column-wise)
pd.concat([df1,df2],axis=0) --- vertical concatenation


ignore index = true --- ignore the index and create a new index
ignore index = false --- keep the index as it is


"""


import pandas as pd

# region1
df_Region1 = pd.DataFrame({
'CustomerID' : [1,2],
'Name': ['Gopal', 'Raju']

})

# region2
df_Region2 = pd.DataFrame({
'CustomerID' : [3,4],
'Name': ['Shyam', 'Baburao']

})

# concat vertical
df_concat = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat)