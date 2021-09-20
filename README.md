## API REST con Django REST Framework y PostgreSQL

Este proyecto es un API REST con Django REST Framework y PostgreSQL, incluye:
- Migraciones iniciales
- Documentación con swagger
- Coleccion de postman para conectar a la API

### Configuración Inicial

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
    source env/bin/activate
    ```
4. Instalar librerías
    ```
    (env) pip install -r requirements.txt 
    ```
5. Verificar datos de conexión a la BD en:

    `api_rest/api_rest/settings/local.py`
    
6. Es necesario crear la base de datos con postgresql, o tambien se puede cambiar la configuración en `api_rest/api_rest/settings/local.py` para usar sqlite3 
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
   }
   ```

7. Correr migraciones
    
   ```
   (env) cd api_rest/
   
   (env) python3 manage.py migrate
   
   ```

8. Crear super usuario para ingresar al admin y crear datos de prueba 
    ```
    (env) python3 manage.py createsuperuser
    ```
9. Ejecutar el servidor:
    ```
    (env) python3 manage.py runserver 
    ```
