"""
Django settings for sds project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LIBS_DIR = os.path.dirname(BASE_DIR)
ROOT_DIR = os.path.dirname(LIBS_DIR)
DATA_DIR = ROOT_DIR+"/data"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*9l5h*%z05)_1!ee0!#!*a8fia((gtdj*+a24c8geo+lk@5dd0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sds_site.urls'

WSGI_APPLICATION = 'sds_site.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "sds/templates")
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR+"/static/",
    BASE_DIR+"/sds/static/",
)



import sys

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info("Python path:    "+repr(sys.path))
log.info("BASE_DIR %s"%(BASE_DIR))
log.info("LIBS_DIR %s"%(LIBS_DIR))
log.info("ROOT_DIR %s"%(ROOT_DIR))
log.info("DATA_DIR %s"%(DATA_DIR))
log.info("TEMPLATE_DIRS %s"%(TEMPLATE_DIRS))

