import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
os.makedirs('data', exist_ok=True)

df = pd.DataFrame(data)

row1 = {'Name': 'David', 'Age': 40, 'City': 'Houston'}
df.loc[len(df.index)] = row1

row2 = {'Name': 'Eva', 'Age': 28, 'City': 'Phoenix'}
df.loc[len(df.index)] = row2

file_path = os.path.join('data', 'people.csv')
df.to_csv(file_path, index=False)
print(f"File '{file_path}' created successfully.")  