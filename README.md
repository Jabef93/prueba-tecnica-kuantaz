# Prueba técnica python-flask desarrollador backend 

## Objetivo

- Realizar una API Rest con su base de datos respectiva para 3 entidades:
  - Instituciones
  - Proyectos
  - Usuarios


## Pruebas funcionales

### Ambiente virtual

Se recomienda utilizar un ambiente virtual con `Python 3.9.13`
  ```bash
    python -m venv <path/nombre_venv>
  ```
Activar ambiente virtual
  ```bash
    source <path/nombre_venv>/Scripts/activate
  ```
Instalar dependencias (las versiones de las dependencias utilizadas se encuentran en `requirements.txt`)
  ```bash
    pip install -r requirements.txt
  ```

### Base de datos

Se utiliza una base de datos PostgreSQL 15.2. Ya está definido el archivo `docker-compose.yml`, por lo que se recomienda utilizar Docker para levantar la base de datos. En este archivo se define la imagen `postgres:15.2-alpine`. Para crear el contenedor y la imagen utilizar el siguiente comando.
  ```bash
    docker-compose up -d
  ```

### Variables de ambiente

Las variables de ambiente se definen en un archivo `.env`. A continuación se muestra un ejemplo
```
SECRET_KEY=PASSWORD
PGSQL_HOST=localhost
PGSQL_USER=postgres
PGSQL_PASSWORD=postgres
PGSQL_DATABASE=postgres
PGSQL_PORT=5432
```

### Iniciar el servidor

  ```bash
    python run.py
  ```
Durante la creación de la aplicación, se realiza a su vez la creacion de las tablas y relaciones de la base de datos mediante el método `create_all` de `flask_sqlalchemy`. Si las tablas y relaciones ya existen no vuelven a crearse. 

El servidor corre en la dirección [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Uso de la API
La documentación se encuentra en el archivo Postman `Prueba Tecnica Kuantaz.postman_collection.json` el cual puede ser importado en Postman para su análisis.
