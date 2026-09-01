### Problem Statements
1- select specific cikunb
2- filter rows
3- combine multiple conditions


### Soluntions

1- Square brackets
2-Boolean conditions

### Selecting specific columns
1- a series
2 - dataframe miltiple colmuns of data


column = df.["column_name"]   # for single column
subset = df[["column1", "column2"]]  # for multiple columns

### Filtering rows
1- Boolean indexing


#### Based on a single condition
filtered_df = df[df["salary"] > 50000]


#### Combining multiple conditions
filtered_rows = df[(df["salary"] > 50000) & (df["department"] == "IT")]



