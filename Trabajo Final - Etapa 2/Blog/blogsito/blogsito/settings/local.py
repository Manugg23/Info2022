from .base import *

SECRET_KEY = 'django-insecure-)ab!vnjnxl7ig6csn9snw$i00r#1gi$8jx06p&whkq&n7l(adl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
