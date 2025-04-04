"""
Django settings for inventory_system project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


from dotenv import load_dotenv
import os

load_dotenv()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = True

ALLOWED_HOSTS = ['www.stockord.win', 'stockord.win', '13.214.241.49', '*']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django_recaptcha',
    'dashboard_view',
    'inventory_view',
    'login_view',
    'procurement_view',
    'supplier_view',
    'pos_view',
    'profile_view',
    'csp', # Content Security Policy
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise Middleware
    # Lock user after multiple failed attempts
    'middleware.IPLockMiddleware',

    # Check user permission and role
    'middleware.PermissionMiddleware',

    # Content Security Policy
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'inventory_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'inventory_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Login Url
LOGIN_URL = "/login/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# RECAPTCHA KEYS from Google Recaptcha (Project Name: Account Mamangement Project EXP).
# Documentation: https://pypi.org/project/django-recaptcha/
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')


CSP_CONNECT_SRC = ("'self'",)  # API sources
CSP_FRAME_SRC = ("https://www.google.com")  # Prevent framing unless necessary

# CONTENT SECURITY POLICY
CSP_DEFAULT_SRC = ("'self'",f"https://stockords3.s3.amazonaws.com")
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://unpkg.com",
    "https://cdn.jsdelivr.net",
    "https://www.google.com",       # Allow reCAPTCHA scripts
    "https://www.gstatic.com",
    "https://stockords3.s3.amazonaws.com",
    "https://stockords3.s3-ap-southeast-1.amazonaws.com",  # Region-specific S3 URL
    # '*', #For Debugging only
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",  # Needed for inline styles
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    "https://fonts.googleapis.com",  # Add this to allow Google Fonts
    "https://stockords3.s3.amazonaws.com",
    "https://stockords3.s3-ap-southeast-1.amazonaws.com",  # Region-specific S3 URL
    # '*', #For Debugging only
)
CSP_IMG_SRC = ("'self'", "data:", "https://stockords3.s3.amazonaws.com", "https://stockords3.s3-ap-southeast-1.amazonaws.com","https://stockords3.s3.amazonaws.com/images/")  # Image sources
CSP_FONT_SRC = (
    "'self'", 
    "https://fonts.googleapis.com", 
    "https://fonts.gstatic.com",
    "https://cdn.jsdelivr.net"
    # '*', #For Debugging only
)  

CSP_STYLE_SRC_ELEM = CSP_STYLE_SRC




# Whitenoise settings
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Set the static files URL path
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # This should point to your 'staticfiles' folder
# # Set STATICFILES_DIRS to the path where your static files are located


# # Optional: Configure admin media files path
# ADMIN_MEDIA_PREFIX = '/static/admin/'
# # Media URL for user-uploaded files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_S3_REGION_NAME = 'ap-southeast-1'  # e.g., 'us-east-1'
AWS_QUERYSTRING_AUTH = False  # Disable query parameter authentication for static files

# Use S3 for static files
STATIC_URL = f'https://stockords3.s3.amazonaws.com/'
# MEDIA_URL = f'https://stockords3.s3.amazonaws.com/images/'
# Use S3 for static file storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CSRF_TRUSTED_ORIGINS = [
    "https://stockord.win",
    "https://www.stockord.win",  # Include both if applicable
]