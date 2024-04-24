import sqlite3

conn = sqlite3.connect('Desnutricion.db')

cursor = conn.cursor()

_SQL = """
CREATE TABLE IF NOT EXISTS Desnutricion (
ORDEN TEXT,
fec_not TEXT,
SEMANA_EPIDEMIOLOGICA TEXT,
AÑO TEXT,
GRUPO_ETARIO TEXT,
CURSO_DE_VIDA TEXT,
SEXO TEXT,
area_ TEXT,
BARRIO TEXT,
NUM_COMUNA TEXT,
TIPO_DE_SEGURIDAD_SOCIAL TEXT,
cod_ase_ TEXT,
aseguradora TEXT,
ESTRATO TEXT,
EDEMA TEXT,
DELGADEZ TEXT,
PIEL_RESECA TEXT,
hiperpigm TEXT,
cambios_cabello TEXT,
PALIDEZ TEXT,
DEPARTAMENTO TEXT,
MUNICIPIO TEXT,
zscorept_aprox TEXT,
INTERPRETACIÓN_ZSCORE_PT TEXT);
"""
cursor.execute(_SQL)


with open('sql.sql', 'r',encoding="UTF-8") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()