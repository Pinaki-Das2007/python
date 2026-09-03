# sorting data
# sorting data 1 column sort_alues()
# df.sort_values(by='column_name', ascending=True, inplace=True)

import pandas as pd
data = {
    "Name":['Arun','Varun','Karun'],
    "Age": [28, 34, 22],
    "Salary": [50000, 60000, 70000]
}


df= pd.DataFrame(data)
df.sort_values(by='Age', ascending=False, inplace=True)
print("Sorted Age by Descending order:")
print(df)