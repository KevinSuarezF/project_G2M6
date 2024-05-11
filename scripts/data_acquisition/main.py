import pandas as pd
df = pd.read_csv('src/nombre_paquete/database/vehicles_colombia.csv')
info = df.info()

data_dict = {}

index_range = f"{df.index.name}: {df.index.start} to {df.index.stop - 1} entries"
data_dict['RangeIndex'] = index_range

columns_dict = {}

for col in df.columns:
    columns_dict[col] = {
        'Non-Null Count': df[col].count(),
        'Dtype': df[col].dtype
    }

data_dict['Data columns'] = columns_dict

#Visualizacion del diccionario
print("Información del DataFrame:")
print("------------------------------------------")
print(f"RangeIndex: {index_range}\n")

print("Data columns (total {} columns):".format(len(df.columns)))
print("------------------------------------------")
for col, col_info in columns_dict.items():
    print(f"#{df.columns.get_loc(col)}   {col}:")
    print(f"{' ' * 6}{'Non-Null Count':<20}: {col_info['Non-Null Count']}")
    print(f"{' ' * 6}{'Dtype':<20}: {col_info['Dtype']}\n")