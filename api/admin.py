# 2

from django.contrib import admin
from .models import Company

admin.site.register(Company)


# Comando para levantar servidor:
# 1. [python manage.py migrate]
# 2. [python manage.py makemigrations]
# 3. de nuevo para crear la TABLA: [python manage.py migrate]

# 4. Para el Login, iniciar sección:
# comando -> [python manage.py createsuperuser]
# _ Username: williams392
# _ email: v_s392@gmail.com
# _ Password: l_5

# 5. Activar el servidor: [python manage.py runserver]

