### Configuración Inicial

Este proyecto es un API REST con Django REST Framework y PostgreSQL, incluye las migraciones iniciales.

1. Clonar repositorio

    ```
    git clone https://github.com/LisethCastillo0325/api-rest-drf.git
    ```

2. Crear entorno virtual

    ```
    virtualenv env
    ```

3. Ativar entorno virtual
    ```
    (env) source env/bin/activate
    ```
4. Instalar librerías
    ```
    (env) pip install -r requirements.txt 
    ```
5. Crear BD 
    ```
    CREATE DATABASE db_apirest;
    ```
6. Verificar datos de conexión a la BD en:

    `api_rest/api_rest/settings/local.py`

7. Crear super usuario
    ```
    (env) python3 manage.py createsuoeruser
    ```
8. Ejecutar el servidor:
    ```
    (env) python3 manage.py runserver 
    ```
