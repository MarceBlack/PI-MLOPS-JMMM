# Proyecto Individual Henry Nº1
### Jorge Marcelo Mendez Mendez



## INTRODUCCION
El proyecto consistía en situarse en el rol de Data Engineer, a quien como miembro del equipo de una empresa, el Tech Lead le solicita realizar un proceso de ETL sobre cuatro datasets proporcionados, conteniendo información relativa a los catálogos de series y películas de cuatro plataformas de streaming (Netflix, Amazon Prime Video, Disney y Hulu ).

Asimismo, se solicitó elaborar una API con un framework de FastAPI, a efectos de disponer los datos en línea, bajo cinco consultas predefinidas.

Tambien, se solicitó documentar todo el proceso y el funcionamiento de la API, asi como también, realizar un video a ser remitido al Tech Lead, quien nos encargó el proyecto para que, nos efectúen un feedback sobre el mismo.

# Propuesta de trabajo (requerimientos de aprobación)

## Transformaciones: 
Para este MVP no necesitas perfección, ¡necesitas rapidez!⏩Vas a hacer estas, y solo estas, transforma a los datos:

> Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los conjuntos de datos (ejemplo para títulos de Amazon = as123)

> Los valores nulos del campo rating deberán reemplazarse por la cadena “G” (corresponde al rating de madurez: “general para todos los públicos”

> De haber fechas, debe tener el formato AAAA-mm-dd

> Los campos de texto deben estar en minúsculas, sin excepciones

> El campo de duración debe convertirse en dos campos: duración_int y duración_tipo. El primero será un entero y el segundo una cadena indicando la unidad de medición de duración: min (minutos) o temporada (temporadas)

## Desarrollo API: Propone disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propone son las siguientes:

> Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(año, plataforma, duración_tipo))

> Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

> Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(plataforma))

> Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))

## Deployment: 
Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil😄. Tambien podrias usar Railway, pero ten en cuenta que con este si necesitas dockerizacion.

## Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores no obstante👀), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Sabes que puedes apoyarte en librerías como pandas profiling, sweetviz, autoviz, entre otros y sacar de allí tus conclusiones😉

## Sistema de recomendación:

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dio un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendaciones debe ser implementado para tener una interfaz gráfica amigable para ser utilizado, utilizando Gradio para su implementación o bien con alguna solución como Streamlit o algo similar en local (tener el implementación del sistema de recomendaciones o una interfaz gráfica es un plus al proyecto).

Video: ¡Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video que muestra el resultado de las consultas propuestas y de tu modelo de ML perturba!

## Tareas realizadas:

# API


# Video de demostración
