import os
from pathlib import Path
from decouple import config
import dj_database_url

# Récupération des variables d'environnement via decouple
ENVIRONMENT = config('ENVIRONMENT', default='production')
DATABASE_URL = config('DATABASE_URL')

# Définir le mode DEBUG en fonction de l'environnement
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration des paramètres de base de Django
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend-production-6ee5.up.railway.app']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    ############################
    'api',
    'corsheaders',
    'rest_framework',
    'dj_rest_auth',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    # 'allauth.account.middleware.AccountMiddleware'
]

SITE_ID = 1

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'backend.wsgi.application'

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRES_LOCALLY = True
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY:
    DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Paramètres de localisation
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuration de la clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentification via Allauth
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

REST_USE_JWT = True

ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True

# Configuration des fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# CORS
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'https://backend-production-6ee5.up.railway.app',
    'https://elmarchi-front-git-main-niscoos-projects.vercel.app',

]

CORS_ALLOWED_ORIGINS = [
    "https://elmarchi-front-git-main-niscoos-projects.vercel.app",  # URL de votre frontend
    "https://elmarchi-front.vercel.app",
    "http://localhost:3000"
]

CORS_ALLOW_CREDENTIALS = True
