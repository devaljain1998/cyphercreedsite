"""
Django settings for cyphercreed project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qijn+)c(k97g@1yqfm0wf)aaqf+8jd0293co)&l#v_axx+8f+j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'markdownify',
    'taggit',
    'blog.apps.BlogConfig',
    'discussion.apps.DiscussionConfig',
    'misc.apps.MiscConfig',
    'userprofile.apps.UserprofileConfig',
    'actions.apps.ActionsConfig',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
TAGGIT_CASE_INSENSITIVE = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_REDIRECT_URL = '/adminBlog'
ROOT_URLCONF = 'cyphercreed.urls'
LOGOUT_URL	=	'logout'
LOGIN_URL = '/profile/login'

#EMAIL_BACKEND	=	'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST	=	'smtp.gmail.com'
EMAIL_HOST_USER	=	'cyphercreedcommunity@gmail.com' 
EMAIL_HOST_PASSWORD	=	'coreonly' 
EMAIL_PORT	=	587 
EMAIL_USE_TLS	=	True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates','templates/blog',],  #'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cyphercreed.wsgi.application' #'wsgi.application'  


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES	=	{
    'default':	{
    'ENGINE':'django.db.backends.postgresql_psycopg2',#django.db.backends.postgresql
    'NAME':	'cyphercreed',								
    'USER':	'postgres',								
    'PASSWORD':	'root',								
    'HOST':	'127.0.0.1',								
    'PORT':	'5432',
} }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
