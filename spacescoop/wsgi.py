"""
WSGI config for spacescoop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spacescoop.settings")
os.environ.setdefault('DJANGO_SETTINGS_CONFIG', 'PROD')

application = get_wsgi_application()
