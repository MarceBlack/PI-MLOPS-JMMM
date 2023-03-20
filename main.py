import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Importar el dataset
streaming_ratings_df = pd.read_csv("streaming_ratings.csv")

# Mensaje de bienvenida
@app.get("/")
async def root():
    return {"message": "Bienvenido a mi API de streaming de películas"}

# Consulta 1: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
@app.get("/max_duration")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    """
    Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
    """
    # Crear una copia del dataframe para no modificar el original
    df_filtered = streaming_ratings_df.copy()
    
    # Filtrar por año
    if year is not None:
        df_filtered = df_filtered[df_filtered["year"] == year]
    else:
        return "Debes ingresar un año."
        
    # Filtrar por plataforma
    if platform is not None:
        df_filtered = df_filtered[df_filtered["platform"] == platform.lower()]
    else:
        return "Debes ingresar una plataforma."
 
    # Filtrar por tipo de duración
    if duration_type is not None:
        if duration_type.lower() == "min":
            df_filtered = df_filtered[df_filtered["duration_min"].notnull()]
            max_duration_col = "duration_min"
        elif duration_type.lower() == "season":
            df_filtered = df_filtered[df_filtered["duration_seasons"].notnull()]
            max_duration_col = "duration_seasons"
        else:
            return "Tipo de duración inválido."
    else:
        # Si no se especifica, se usa la duración más larga (entre minutos y temporadas)
        df_filtered = df_filtered[df_filtered["duration_min"].notnull() | df_filtered["duration_seasons"].notnull()]
        max_duration_col = "duration_max"
    
    # Encontrar la película con la duración máxima
    max_duration_idx = df_filtered[max_duration_col].idxmax()
    max_duration_movie = df_filtered.loc[max_duration_idx, :]
    
    return "hola"

# Consulta 2: Cantidad de películas por plataforma y filtrar plataforma, score promedio y año indicados
@app.get('/score_count/')
def get_score_count(platform: str, scored: float, year: int = None):
    # Filtrar los datos según los valores de los parámetros
    filtered = streaming_ratings_df.copy()
    filtered = filtered[filtered['platform'] == platform]
    if year is not None:
        filtered = filtered[filtered['year'] == year]
    
    # Contar la cantidad de películas por plataforma y devolver los resultados
    count = len(filtered[filtered['scored'] > scored])
    return {'count': count}

# Consulta 3: Cantidad de películas por plataforma y filtrar los resultados según la plataforma indicada
@app.get('/count_platform/')
def get_count_platform(platform: str):
    count = len(streaming_ratings_df[streaming_ratings_df['platform'] == platform])
    return {'count': count}

# Consulta 4: Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get('/actor/')
def get_actor(platform, year):
    # Filtrar por plataforma y año
    df_filtered = streaming_ratings_df[(streaming_ratings_df['platform'] == platform) & (streaming_ratings_df['year'] == year)]
    # Concatenar los valores de la columna "cast"
    cast_values = df_filtered['cast'].str.cat(sep=',').split(',')
    # Contar la frecuencia de cada actor
    actor_count = pd.Series(cast_values).value_counts()
    # Obtener el actor con mayor frecuencia
    most_common_actor = actor_count.idxmax()
    return most_common_actor

