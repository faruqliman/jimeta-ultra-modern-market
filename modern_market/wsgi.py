import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modern_market.settings')

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)