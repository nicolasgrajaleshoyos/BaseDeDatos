import pandas as pd


df = pd.read_csv('Desnutricion.csv')


tabla = "CREATE TABLE IF NOT EXISTS Desnutricion (\n"
for column in df.columns:
    column_name = column.replace(" ", "").replace("/", "").replace("(", "").replace(")", "").replace(":", "_")   
    tabla += column_name + " TEXT,\n"
tabla = tabla[:-2]  
tabla += ");\n"

print(tabla)


insert = "INSERT INTO Desnutricion("
for column in df.columns:
    column_name = column.replace(" ", "").replace("/", "").replace("(", "").replace(")", "").replace(":", "_")     
    insert += column_name + ", "
insert = insert[:-2] 
insert += ") VALUES\n"

for index, row in df.iterrows():
    insert += "("
    for column in df.columns:
        insert += "'" + str(row[column]) + "', "
    insert = insert[:-2]  
    insert += "),\n"

insert = insert[:-2]  
insert += ";\n"

print(insert)


with open("sql.sql", "w", encoding="UTF-8") as f:
    f.write(insert)