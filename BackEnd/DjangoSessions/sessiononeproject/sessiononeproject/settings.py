"""
Django settings for sessiononeproject project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
print(os.environ.get("path"))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
"""
The line BASE_DIR = Path(__file__).resolve().parent.parent sets the base directory of your Django project. Here is what this line does:

__file__: __file__ is a built-in Python variable that contains the path to the current file. In this case, it contains the path to the settings.py file.

Path(): Path() is a class provided by Python's built-in pathlib module that represents a filesystem path. The Path() function creates a Path object from the string __file__.

.resolve(): The .resolve() method of a Path object returns the absolute path of the file.

.parent: The .parent attribute of a Path object returns the parent directory of the file.

.parent (again): The second .parent attribute returns the parent directory of the parent directory, which is the root directory of the project.

So, putting all of this together, BASE_DIR is set to the root directory of your Django project.

This is helpful because it allows you to easily reference files and directories within your project, regardless of where the project is located on the filesystem. For example, if you have a file named example.txt in a directory named data within your project, you can reference it using the BASE_DIR variable like this:

file_path = BASE_DIR / 'data' / 'example.txt'

This makes your code more portable, since it will work even if you move the project to a different directory or machine.
"""
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e+)8611*g%s@c+h^&5!itw55dc(6uy%)!@h=zwcleyb767+n_h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
'''
django.contrib.admin: Provides an admin interface for managing site content and user accounts.
django.contrib.auth: Provides user authentication and authorization functionality.
django.contrib.contenttypes: Provides a framework for working with different types of content in a Django project.
django.contrib.sessions: Provides a session framework for managing user sessions.
django.contrib.messages: Provides a framework for displaying messages to the user, such as success messages or error messages.
django.contrib.staticfiles: Provides a framework for managing static files, such as CSS, JavaScript, and image files.
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

'''
ROOT_URLCONF is a configuration setting in Django that specifies the Python module where the URL patterns for the project are defined. When a URL is requested, Django uses the patterns defined in this module to determine which view function to call to handle the request.
'''
ROOT_URLCONF = 'sessiononeproject.urls'


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

WSGI_APPLICATION = 'sessiononeproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
