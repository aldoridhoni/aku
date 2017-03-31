# Django settings for aku project.

import os.path

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']

SETTINGS_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(SETTINGS_PATH)

ADMINS = (('Fitra Aditya', 'aditya.fp@gmail.com'), )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'aku.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Jakarta'

LANGUAGE_CODE = 'id'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_PATH, 'media'))

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '!(p&y-8f6gdtdfzn7qp7f0b+yw*l+)caeept1rl7v$zqaz7o23'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_PATH, 'aku', 'templates'), ],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader'
        ]
    },
}, ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'aku.urls'

INSTALLED_APPS = [
    'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.sites',
    'django.contrib.messages', 'django.contrib.admin',
    'django.contrib.staticfiles', 'django_openid_auth', 'openid_provider',
    'main', 'profile', 'debug_toolbar'
]

DEFAULT_AVATAR = os.path.join(MEDIA_ROOT, 'generic.jpg')
GRAVATAR = True

AVATAR_WEBSEARCH = True

# 127.0.0.1:8000 Google Maps API Key
GOOGLE_MAPS_API_KEY = ""

AUTH_PROFILE_MODULE = 'profile.profile'

DEFAULT_FROM_EMAIL = 'username@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True

ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = '/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WSGI_APPLICATION = 'aku.wsgi.application'
STATIC_URL = '/static/'
