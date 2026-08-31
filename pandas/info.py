import pandas as pd



data = {
    "Name":['Ram','Shyam','Gopal'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']
}
# df = pd.read_json("pandas/sample_Data.json")
df = pd.DataFrame(data)
print("Displaying the info of dataset")
print(df.info())


