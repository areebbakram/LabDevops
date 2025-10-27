# """
# Django settings for django_devops_lab project.
# """

# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-secret-key')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG') == '1'

# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split()

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # Local apps
#     'core',
# ]


# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'django_devops_lab.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'django_devops_lab.wsgi.application'


# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.postgresql'),
#         'NAME': os.getenv('SQL_DATABASE', 'django_db'),
#         'USER': os.getenv('SQL_USER', 'django_user'),
#         'PASSWORD': os.getenv('SQL_PASSWORD', 'django_pass'),
#         'HOST': os.getenv('SQL_HOST', 'db'),
#         'PORT': os.getenv('SQL_PORT', '5432'),
#     }
# }


# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]


# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True


# # Static files
# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


"""
Django settings for django_devops_lab project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == '1'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split()

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_devops_lab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_devops_lab.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('SQL_DATABASE', 'django_db'),
        'USER': os.getenv('SQL_USER', 'django_user'),
        'PASSWORD': os.getenv('SQL_PASSWORD', 'django_pass'),
        'HOST': os.getenv('SQL_HOST', 'db'),  # matches GitHub Action service name
        'PORT': os.getenv('SQL_PORT', '5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
