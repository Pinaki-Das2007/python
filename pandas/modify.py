import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam','Dhansyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}


df = pd.DataFrame(data)

print(df)

df["Bonus"]= df["Salary"] * 0.1
print(df)



#  using insert method at a specific location
# df.insert(loc , "cloumn_name","some_data")

df.insert(0,"Employee Id", [101,102,103,104,105,106,107,108])
print(df)