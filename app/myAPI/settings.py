from pathlib import Path
from dotenv import load_dotenv
import os
import environ
load_dotenv()

# Initialize the environment variables using django-environ
env = environ.Env()
# Set the path for .env
env_file_path = Path(__file__).resolve().parent.parent / '.env'

# Read the .env file
environ.Env.read_env(env_file_path)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  # Secret key fetched from the .env file
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)  # Debug mode (default is True) from .env file
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1', '0.0.0.0'])  # Allowed hosts for the application

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin interface
    'django.contrib.auth',  # Django authentication framework
    'django.contrib.contenttypes',  # Django content types framework
    'django.contrib.sessions',  # Django sessions framework
    'django.contrib.messages',  # Django messaging framework
    'django.contrib.staticfiles',  # Django static files framework
    'rest_framework',  # Django REST framework for building APP_DIRS
    'rest_framework.authtoken',
    'myapp',  # Your custom application (replace with your app name)
    'ecommerce', # new application
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # Cross-site request forgery middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection middleware
]

# URL configuration
ROOT_URLCONF = 'myAPI.urls'  # URL configuration module

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine backend
        'DIRS': [],  # Directories where templates are located
        'APP_DIRS': True,  # Automatically look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Messaging context processor
            ],
        },
    },
]

# WSGI application for deployment
WSGI_APPLICATION = 'myAPI.wsgi.application'  # WSGI application callable

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # This will create a file named db.sqlite3 in your project root
    }
}



# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validate user attributes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validate minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validate against common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validate numeric passwords
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Language code for the application
TIME_ZONE = 'UTC'  # Time zone for the application
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable time zone support

# Static files (CSS, JavaScript, Images) settings
STATIC_URL = 'static/'  # URL prefix for static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default primary key field type


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'SEARCH_PARAM': 'filter[search]',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}
