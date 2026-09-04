# df["column name"].mean() - mean of the column
# df["column name"].sum() - sum of the column
# df["column name"].max() - max of the column


import pandas as pd
data = {
    "Name":['Arun','Varun','Karun'],
    "Age": [28, 34, 22],
    "Salary": [50000, 60000, 70000]
}


df= pd.DataFrame(data)


max_salary = df["Salary"].max()
print(max_salary)

min_salary = df["Salary"].min()
print(min_salary)

avg_salary = df["Salary"].mean()
print(avg_salary)

sum_salary = df["Salary"].sum()
print(sum_salary)