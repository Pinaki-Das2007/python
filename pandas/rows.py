# head() tail()
# head() returns first 5 rows
# tail() returns last 5 rows



import pandas as pd

df = pd.read_json("pandas\sample_Data.json")
print('Displaying the first 10 rows')
print(df.head(10))


print('Displaying the last 10 rows')
print(df.tail(10))