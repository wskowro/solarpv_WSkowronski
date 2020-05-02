"""
WSGI config for PD6 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PD6.settings')

os.environ["DB_KEY"]="0*9fp=!pn$j7#0-&w-k(0eqljfs5xuy!dsmyy0o8qs@3_%9ywf"

application = get_wsgi_application()
