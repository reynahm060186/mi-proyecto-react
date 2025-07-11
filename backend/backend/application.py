import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Reemplaza 'tu_proyecto'

application = get_wsgi_application()
