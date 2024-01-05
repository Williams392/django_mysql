
1.  Activar el modo virtual.

        source venv/Scripts/activate -> para Windows
        . env/bin/activate -> Para Mac

2.  Instalar Django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        pip install -r requirements.txt

3. Crear las migraciones y correrlas

        python manage.py makemigrations  -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

4. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000


5. Editar el archivo settings.py del proyecto, cambiando los parametros de conexión a MySQL

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': 'localhost',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD': '',
                'NAME': 'django_restframework',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
            }
        }  

    #####  JSON
    ```json
    [
        {
            "id": 1,
            "name": "Facebook",
            "website": "https://www.facebook.com/",
            "foundation": 2004
        },
        {
            "id": 2,
            "name": "Steam",
            "website": "https://store.steampowered.com/",
            "foundation": 2003
        },
        {
            "id": 3,
            "name": "Instagram",
            "website": "https://www.instagram.com/",
            "foundation": 2010
        }
    ]
    ```
    ##### Base de Datos

    <a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Kj8KXqbg/img-mysql-django.png' border='0' alt='img-mysql-django'/></a>