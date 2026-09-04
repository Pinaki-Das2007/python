"""
pd.merge(df1,df2,on="column_name",how="inner") --- inner join
pd.merge(df1,df2,on="column_name",how="outer") --- outer join
pd.merge(df1,df2,on="column_name",how="left") --- left join
pd.merge(df1,df2,on="column_name",how="right") --- right join
pd.merge(df1,df2,on="column_name",how="cross") --- cross join

"""


import pandas as pd
df_costumer = pd.DataFrame({
    'CustomerId':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']

})


df_orders = pd.DataFrame({
    'CustomerId':[1,2,4],
    'OrderAmount':[250,450,350] 
})

# merge
df_merged = pd.merge(df_costumer,df_orders,on="CustomerId",how="right")
print("Inner Join:" )
print(df_merged)
