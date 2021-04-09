import pandas as pd

df = pd.read_excel(r'Libro_1.xlsx', sheet_name="N_Virginia")

#print(df[:5])

print(df.InstanceType.unique()) # Lista de las categorias