import pandas as pd
reader = pd.read_excel("Name.xlsx")
entry = reader.columns[0]
for row in reader[entry][:]:
    print(row)