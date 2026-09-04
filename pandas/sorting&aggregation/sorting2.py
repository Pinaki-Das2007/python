# df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)
import pandas as pd
data = {
    "Name":['Arun','Varun','Karun'],
    "Age": [28, 34, 22],
    "Salary": [50000, 60000, 70000]
}


df= pd.DataFrame(data)
df.sort_values(by=['Age','Salary'], ascending=[True,False], inplace=True)
print("Sorted Age by Descending order:")
print(df)