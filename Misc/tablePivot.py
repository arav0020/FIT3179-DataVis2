import pandas as pd

file = '../Data/worldGDP_converted.csv'

# Assuming you have loaded your CSV file into a DataFrame
df = pd.read_csv(file)

# Pivoting the table: rows as 'Entity' and 'Code', columns as 'Year', and values as 'GDP'
pivot_df = df.pivot(index=["Entity", "Code"], columns="Year", values="GDP").reset_index()

# Display or save the pivoted DataFrame
print(pivot_df)

# Optionally, save the output to a CSV file
pivot_df.to_csv(file, index=False)
