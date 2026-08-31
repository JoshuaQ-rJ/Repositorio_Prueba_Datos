# 🚗 Analisis de ventas automotriz: End-to-End Data Pipeline & Dashboard

## 📌 Descripción

**Automobile Sales Analytics** es una solución integral (*end-to-end*) de ingeniería y analítica de datos. El proyecto abarca desde la ingesta de un conjunto de datos en estado bruto sobre ventas de automóviles, su procesamiento y saneamiento con Python, la estructuración de los datos en PostgreSQL (desplegado mediante Docker), hasta la creación de un tablero interactivo en Power BI.

---

## 🎯 Objetivo

Desarrollar una solución funcional de procesamiento y análisis de datos orientada a la toma de decisiones en el sector automotriz.

El pipeline permite:

- Detectar y tratar inconsistencias en los datos.
- Limpiar y transformar la información mediante Pandas.
- Estructurar los datos para su análisis en PostgreSQL.
- Separar información de hechos y dimensiones.
- Conectar la base de datos con Power BI.
- Construir indicadores y visualizaciones para responder preguntas de negocio.

---

## 🏢 Contexto de negocio

El proyecto fue desarrollado en el marco de la **Prueba de Desempeño Analítica de Datos M5.7 - Cohorte 7**.

La solución aborda una problemática común en las organizaciones: la existencia de datos operacionales con inconsistencias, duplicados, valores faltantes y formatos no estandarizados.

En este caso, la información corresponde a ventas de automóviles distribuidas por diferentes sedes y características de los vehículos, permitiendo analizar variables como:

- Marca.
- Tipo de carrocería.
- Tipo de combustible.
- Precio público.
- Cantidad vendida.
- Fecha de venta.
- Sede.
- Ingresos.
- Margen.

El objetivo final es transformar datos sin procesar en información útil para el análisis comercial y la toma de decisiones.

---

## 🧰 Tecnologías utilizadas

| Categoría | Tecnología | Uso en el proyecto |
| :--- | :--- | :--- |
| **Lenguaje** | Python 3 | Desarrollo del pipeline de procesamiento. |
| **Procesamiento** | Pandas | Limpieza, transformación y preparación de datos. |
| **Conexión SQL** | SQLAlchemy | Conexión y carga de información hacia PostgreSQL. |
| **Driver PostgreSQL** | psycopg2 | Comunicación entre Python y PostgreSQL. |
| **Base de datos** | PostgreSQL | Almacenamiento estructurado de los datos. |
| **Contenedores** | Docker / Docker Compose | Despliegue del entorno de PostgreSQL. |
| **Visualización** | Power BI Desktop | Construcción del dashboard interactivo. |
| **Variables de entorno** | python-dotenv | Gestión de parámetros y credenciales mediante `.env`. |

---

## 📂 Estructura del proyecto

```text
├── env/                                             # Entorno virtual de Python
├── __pycache__/                                     # Archivos compilados de Python
├── .env                                             # Variables de entorno locales
├── .env.example                                     # Plantilla de variables de entorno
├── Automobile_ventas_practica_1000_FILAS_SUCIO.csv # Dataset original
├── Automobile_ventas_practica_LIMPIO.csv            # Dataset limpio
├── dim_sedes.csv                                    # Datos de la dimensión de sedes
├── hechos_ventas_autos.csv                          # Datos de hechos de ventas
├── docker-compose.yml                               # Configuración de Docker
├── limpieza_datos_panda.py                          # Limpieza y transformación de datos
└── pandas_postgres.py                               # Carga de datos hacia PostgreSQL
```

> **Nota:** En un repositorio Git se recomienda excluir `env/`, `__pycache__/` y `.env` mediante `.gitignore`.

---

## 📊 Dataset

El proyecto utiliza un conjunto de datos de ventas de automóviles con **1.000 registros** y múltiples variables relacionadas con el comportamiento comercial de los vehículos.

### Atributos principales

- **Información del vehículo:** marca, tipo de carrocería y tipo de combustible.
- **Métricas comerciales:** precio público, cantidad vendida e ingresos.
- **Rentabilidad:** margen.
- **Dimensión temporal:** fecha de venta.
- **Dimensión geográfica:** sede.

### Archivos de datos

| Archivo | Descripción |
| :--- | :--- |
| `Automobile_ventas_practica_1000_FILAS_SUCIO.csv` | Dataset de origen con inconsistencias que requiere limpieza. |
| `Automobile_ventas_practica_LIMPIO.csv` | Resultado del proceso de limpieza y transformación. |
| `dim_sedes.csv` | Datos correspondientes a la dimensión de sedes. |
| `hechos_ventas_autos.csv` | Información de hechos y métricas relacionadas con las ventas. |

---

## 🧹 Limpieza y transformación

El proceso de limpieza se encuentra principalmente en:

```text
limpieza_datos_panda.py
```

El objetivo es transformar el dataset original en información consistente y preparada para su posterior análisis.

Entre las validaciones y transformaciones consideradas se encuentran:

- Exploración inicial del dataset.
- Revisión de estructura, columnas y tipos de datos.
- Identificación de valores nulos.
- Tratamiento de valores faltantes en campos relevantes.
- Eliminación de registros duplicados.
- Estandarización de fechas.
- Normalización de valores de texto.
- Homogeneización de categorías.
- Revisión de valores numéricos.
- Identificación de cantidades negativas o inválidas.
- Revisión de precios fuera de rango o no válidos.
- Validación de consistencia de los registros.
- Generación del dataset limpio.

El resultado principal del proceso es:

```text
Automobile_ventas_practica_LIMPIO.csv
```

---

## 🗄️ Modelado de datos

Los datos procesados se organizan para facilitar su almacenamiento y análisis.

La estructura contempla una separación entre información de hechos y dimensiones, siguiendo el concepto de **modelo dimensional / esquema en estrella**.

### Tabla de hechos

**`hechos_ventas_autos`**

Contiene información relacionada con las operaciones de venta y sus principales métricas.

Entre las métricas analizadas se encuentran:

- Ingresos.
- Precio público.
- Cantidad vendida.
- Margen.

### Dimensión de sedes

**`dim_sedes`**

Contiene información descriptiva relacionada con las sedes comerciales.

### Representación conceptual

```text
[ dim_sedes ]
       │
[ dim_marcas ]
       │
[ dim_carrocerias ]
       │
[ dim_combustibles ]
       │
[ dim_paises_origen ]
       │
       ▼
[ hechos_ventas_autos ]
       │
       └── Métricas de ventas
```

> La estructura conceptual puede ampliarse según el modelo implementado en PostgreSQL.

---

## 🐘 PostgreSQL y 🐳 Docker

PostgreSQL funciona como repositorio estructurado para los datos procesados.

El archivo:

```text
docker-compose.yml
```

permite configurar el servicio de PostgreSQL mediante Docker Compose.

El script:

```text
pandas_postgres.py
```

se encarga de establecer la conexión desde Python y realizar la carga de los datos hacia PostgreSQL utilizando las herramientas de conexión definidas para el proyecto.

### Componentes principales

- **PostgreSQL:** almacenamiento de los datos.
- **Docker:** aislamiento y ejecución del entorno.
- **Docker Compose:** configuración y administración del servicio.
- **SQLAlchemy:** conexión desde Python.
- **psycopg2:** driver de PostgreSQL.

---

## 🔄 Pipeline de datos

El flujo general del proyecto es:

```text
┌──────────────────────────────────────────────────────┐
│                  DATASET ORIGINAL                    │
│ Automobile_ventas_practica_1000_FILAS_SUCIO.csv      │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│             LIMPIEZA Y TRANSFORMACIÓN                │
│        limpieza_datos_panda.py + Pandas              │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│              DATOS LIMPIOS Y MODELADOS               │
│  LIMPIO.csv / hechos_ventas_autos.csv / dim_sedes    │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│                  CARGA DE DATOS                      │
│             pandas_postgres.py                       │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│                    POSTGRESQL                         │
│                 Docker / Compose                     │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│                   POWER BI                            │
│          Análisis y visualización                    │
└──────────────────────────────────────────────────────┘
```

---

# 📊 Dashboard en Power BI

El dashboard fue desarrollado en **Power BI** y está orientado al análisis de ventas, ingresos, márgenes y comportamiento comercial.

## 📌 KPIs principales

### 💰 Ventas totales

**≈ $1,95 mil M**

### 🚗 Unidades vendidas

**≈ 159,10 mil**

> Los valores pueden variar dependiendo de los filtros y del conjunto de datos utilizado.

---

## 🎛️ Filtros e interactividad

### Filtro temporal

El dashboard permite filtrar la información por año:

- 2023
- 2024
- 2025
- 2026

### Tipo de carrocería

También se puede segmentar la información por:

- Convertible
- Hardtop
- Hatchback
- Sedan
- Wagon

Esto permite analizar el comportamiento de las métricas bajo diferentes segmentos del portafolio de vehículos.

---

## 📈 Visualizaciones

### 1. Marcas y tipos de carrocería vs. ingreso total

**Tipo:** Gráfico de barras apiladas horizontal.

Permite comparar los ingresos generados por cada marca y observar cómo se distribuyen según el tipo de carrocería.

---

### 2. Margen vs. marca

**Tipo:** Gráfico de columnas.

Permite comparar el margen entre las diferentes marcas y detectar aquellas con mayor contribución a la rentabilidad.

---

### 3. Cantidad vendida por año de venta y sede

**Tipo:** Gráfico de líneas con área.

Permite observar la evolución temporal de las unidades vendidas y comparar el comportamiento de las diferentes sedes.

---

### 4. Promedio de precio público por tipo de combustible

**Tipo:** Gráfico circular.

Permite comparar la distribución del precio público promedio entre:

- Gas.
- Diesel.

En el dashboard analizado, Gas representa aproximadamente **56,17%**, mientras que Diesel representa **43,83%**.

---

## 🎨 Diseño del Dashboard

El dashboard utiliza una estética **Dark Mode** con una identidad visual futurista relacionada con el sector automotriz.

### Características visuales

- Fondo gris oscuro / negro.
- Elementos destacados en rojo tipo neón.
- Texto blanco para facilitar la lectura.
- Tonos grises para información secundaria.
- Diseño basado en una cuadrícula.
- Panel lateral para KPIs y filtros.
- Área principal destinada a las visualizaciones analíticas.

La distribución busca facilitar una lectura rápida de los principales indicadores y permitir posteriormente un análisis más detallado.

---

## ❓ Preguntas de negocio

El dashboard permite responder preguntas como:

| # | Pregunta de negocio | Métrica / análisis | Visualización |
| :---: | :--- | :--- | :--- |
| 1 | ¿Qué marcas generan mayores ingresos y cuál es su mezcla de carrocerías? | Ingreso total por marca y carrocería | Barras apiladas |
| 2 | ¿Qué marcas presentan los mayores márgenes? | Margen por marca | Columnas |
| 3 | ¿Cómo evolucionan las unidades vendidas entre las diferentes sedes? | Cantidad vendida por fecha y sede | Líneas / área |
| 4 | ¿Cuál es el precio público promedio según el tipo de combustible? | Promedio de precio público | Gráfico circular |
| 5 | ¿Cómo cambia el comportamiento de las ventas al seleccionar diferentes períodos? | KPIs y métricas filtradas por año | Segmentadores + KPIs |

Estas preguntas permiten conectar el análisis técnico con necesidades concretas de negocio.

---

## 💡 Insights

A partir de los datos utilizados en el dashboard se identifican los siguientes insights:

### 1. Rentabilidad por marca

Marcas como **BMW, Mercedes-Benz y Porsche** presentan algunos de los márgenes más elevados dentro del portafolio analizado.

### 2. Distribución por combustible

Los vehículos clasificados como **Gas** representan aproximadamente el **56,17%** del promedio de precio público analizado, frente al **43,83%** correspondiente a Diesel.

### 3. Evolución de las ventas

Se observa una tendencia creciente en el volumen de unidades vendidas hacia los períodos más recientes analizados.

> Estos insights corresponden exclusivamente al dataset utilizado en el proyecto y no deben interpretarse como conclusiones generales del mercado automotriz.

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear el entorno virtual

En Windows:

```bash
python -m venv env
```

Activar:

```bash
env\Scripts\activate
```

En Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install pandas sqlalchemy psycopg2-binary python-dotenv
```

### 4. Configurar variables de entorno

Utiliza `.env.example` como referencia para crear tu archivo `.env`.

Ejemplo:

```env
DB_HOST=TU_HOST
DB_PORT=TU_PUERTO
DB_NAME=TU_BASE_DE_DATOS
DB_USER=TU_USUARIO
DB_PASSWORD=TU_PASSWORD
```

**No compartas ni subas el archivo `.env` con credenciales reales.**

---

## ▶️ Ejecución del pipeline

### 1. Levantar PostgreSQL

```bash
docker compose up -d
```

### 2. Ejecutar la limpieza de datos

```bash
python limpieza_datos_panda.py
```

### 3. Cargar los datos en PostgreSQL

```bash
python pandas_postgres.py
```

### 4. Conectar Power BI

En **Power BI Desktop**:

1. Seleccionar **Obtener datos**.
2. Seleccionar **Base de datos PostgreSQL**.
3. Introducir los parámetros correspondientes al servidor y base de datos.
4. Cargar las tablas necesarias.
5. Actualizar el modelo y comenzar el análisis.

### 5. Detener PostgreSQL

Cuando finalice el trabajo:

```bash
docker compose down
```

---

## 🔐 Seguridad y buenas prácticas

- No subir `.env` al repositorio.
- Mantener `.env.example` sin credenciales reales.
- Evitar almacenar contraseñas directamente en los scripts.
- Utilizar variables de entorno para la configuración.
- Excluir `env/` del control de versiones.
- Excluir `__pycache__/` del control de versiones.
- Mantener separados los datos de configuración y el código fuente.

Un `.gitignore` recomendado sería:

```gitignore
.env
env/
__pycache__/
*.pyc
```

---

## 📈 Resultados

La implementación del proyecto permite:

- **Automatizar** el proceso de limpieza y preparación de datos.
- **Mejorar la calidad** de la información utilizada para el análisis.
- **Centralizar** los datos procesados en PostgreSQL.
- **Organizar** la información para facilitar consultas y análisis.
- **Conectar** la base de datos con Power BI.
- **Construir KPIs y visualizaciones** orientadas a la toma de decisiones.
- **Analizar** ingresos, unidades vendidas, márgenes, sedes y características de los vehículos.

---

## 🚀 Flujo resumido

```text
CSV SUCIO
   ↓
PANDAS
   ↓
LIMPIEZA
   ↓
DATASET LIMPIO
   ↓
MODELO DE DATOS
   ↓
POSTGRESQL
   ↓
POWER BI
   ↓
DASHBOARD
   ↓
INSIGHTS DE NEGOCIO
```

---

## 👨‍💻 Autor

Proyecto desarrollado como prueba práctica de desempeño en **Analítica e Ingeniería de Datos M5.7 - Cohorte 7** Por **Joshua Quintero - Coder**.
