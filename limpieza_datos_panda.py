
import pandas as pd
import numpy as np


df = pd.read_csv('Automobile_ventas_practica_1000_FILAS_SUCIO.csv')
duplicados = df.duplicated()
registros_incompletos = df.isnull().sum()
print(df.dtypes)
print(df.describe())
print(f"Registros con datos faltantes: {registros_incompletos}")
print(f"Registros duplicados: {duplicados.sum()}")
df = df.drop_duplicates()
df.columns = df.columns.str.strip()
# Selecciona solo las columnas de texto (object o string)
cols_texto = df.select_dtypes(include=['object', 'string']).columns
df[cols_texto] = df[cols_texto].apply(lambda col: col.str.strip().str.title())


df['Precio_Catalogo_Original'] = df['Precio_Catalogo_Original'].replace('[\$,]', '', regex=True).astype(float)

# Limpiar el año y extraer los 4 dígitos
df['Anio_Venta'] = (
    df['Anio_Venta']
    .astype(str)
    .str.extract(r'(\d{4})')[0]
)

# Convertir a número
df['Anio_Venta'] = pd.to_numeric(
    df['Anio_Venta'],
    errors='coerce'
)

# Convertir el año a datetime
df['Anio_Venta'] = pd.to_datetime(
    df['Anio_Venta'].astype('Int64').astype(str),
    format='%Y',
    errors='coerce'
)

# Rellenar los valores vacíos con la fecha más frecuente
moda = df['Anio_Venta'].mode()

if not moda.empty:
    df['Anio_Venta'] = df['Anio_Venta'].fillna(moda.iloc[0])




df['Ciudad_Sede'] = df['Ciudad_Sede'].str.strip().str.title()
df['Tipo_Combustible'] = df['Tipo_Combustible'].fillna(df['Tipo_Combustible'].mode()[0])
df['Caballos_Fuerza'] = df['Caballos_Fuerza'].fillna(df['Caballos_Fuerza'].mean())
df['Ciudad_Sede'] = df['Ciudad_Sede'].fillna(df['Ciudad_Sede'].mode()[0])
df['Precio_Construccion'] = df['Precio_Construccion'].fillna(df['Precio_Construccion'].mean())
df['Precio_Publico'] = df['Precio_Publico'].replace('[\$,]', '', regex=True).astype(float)
df['Cantidad_Vendida'] = df['Cantidad_Vendida'].replace('U', '', regex=True)
df['Cantidad_Vendida'] = df['Cantidad_Vendida'].replace('nidades', '', regex=True)
df['Cantidad_Vendida'] = df['Cantidad_Vendida'].astype(float)
df['Sede'] = df['Sede'].replace('Primeauto Andiino', 'Primeauto Andino')
df['Sede'] = df['Sede'].replace('Velocitymotors', 'Velocity Motors')
df['Sede'] = df['Sede'].replace('Motorcenter Sur', 'MotorCenter Sur')
df['Sede'] = df['Sede'].replace('Autoplaza Nrote', 'Autoplaza Norte')
df['Sede'] = df['Sede'].replace('Drivehub Caribee', 'Drivehub Caribe')
df['Sede'] = df['Sede'].replace('Velocitymotor', 'Velocity Motors')
df['Sede'] = df['Sede'].replace('Autoplaza Norte', 'Auto Plaza Norte')
df['Sede'] = df['Sede'].replace('Auto Plaza Norte', 'Autoplaza Norte')
df['Sede'] = df['Sede'].replace('Prime Auto Andino', 'Primeauto Andino')
df['Sede'] = df['Sede'].replace('Car World Pacifico', 'Carworld Pacifco')



registros_incompletos = df.isnull().sum()
print(f"Registros con datos faltantes: {registros_incompletos}")
print(df.dtypes)


print(df.head())
print(df['Anio_Venta'].dtype)
df.to_csv('Automobile_ventas_practica_LIMPIO.csv', index=False)

df = pd.read_csv('Automobile_ventas_practica_LIMPIO.csv')

Pais_origen =(df[['Pais_Origen']]).drop_duplicates().reset_index(drop=True)
Pais_origen.insert(0, 'ID_Pais_Origen', np.arange(1, len(Pais_origen) + 1))

carroceria = (df[['Tipo_Carroceria']]).drop_duplicates().reset_index(drop=True)
carroceria.insert(0, 'ID_Tipo_Carroceria', np.arange(1, len(carroceria) + 1))

combustible = (df[['Tipo_Combustible']]).drop_duplicates().reset_index(drop=True)
combustible.insert(0, 'ID_Tipo_Combustible', np.arange(1, len(combustible) + 1))

ciudad = (df[['Ciudad_Sede']]).drop_duplicates().reset_index(drop=True)
ciudad.insert(0, 'ID_Ciudad_Sede', np.arange(1, len(ciudad) + 1))

marcas = (df[['Marca','Pais_Origen']]).drop_duplicates()
marcas.insert(0, 'ID_Marca', np.arange(1, len(marcas) + 1))
marcas = marcas.merge(Pais_origen, on='Pais_Origen', how='left')
marcas = marcas.drop(columns=['Pais_Origen'])

sedes = (df[['Sede','Ciudad_Sede']]).drop_duplicates()
sedes.insert(0, 'ID_Sede', np.arange(1, len(sedes) + 1))
sedes = sedes.merge(ciudad, on='Ciudad_Sede', how='left')
sedes = sedes.drop(columns=['Ciudad_Sede'])
sedes.to_csv('dim_sedes.csv', index=False)
ventas_autos = df.copy()
ventas_autos = ventas_autos.merge(Pais_origen, on='Pais_Origen', how='left')
ventas_autos = ventas_autos.merge(carroceria, on='Tipo_Carroceria', how='left')
ventas_autos = ventas_autos.merge(combustible, on='Tipo_Combustible', how='left')
ventas_autos = ventas_autos.merge(marcas, on='Marca', how='left')
ventas_autos = ventas_autos.merge(sedes, on='Sede', how='left')
ventas_autos = ventas_autos.drop(columns=['Pais_Origen', 'Tipo_Carroceria', 'Tipo_Combustible', 'Marca', 'Sede','Ciudad_Sede'])
duplicados = ventas_autos.duplicated(subset=['ID_Venta'])
ventas_autos = ventas_autos.drop_duplicates(subset=['ID_Venta'])
duplicados = ventas_autos.duplicated(subset=['ID_Venta'])
ventas_autos.to_csv('hechos_ventas_autos.csv', index=False)
print(duplicados.sum())
print(df.describe())








