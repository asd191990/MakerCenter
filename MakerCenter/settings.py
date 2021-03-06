"""
Django settings for MakerCenter project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7%p9qm@(jy0t1zh)38v@@jjmg*6r2)da6%%bzgp4k(g&_p6$2r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 要加在admin前
    'admin_volt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # app
    'BackEnd',
    'FrontEnd',
    # 套件
    'ckeditor',
    'ckeditor_uploader',
    'django_filters',
    'django_cleanup',
    # scss
    'sass_processor',
]

####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_UPLOAD_PATH = 'uploads/'  # 上傳文件的目錄
CKEDITOR_IMAGE_BACKEND = 'pillow'  # pillow做爲backend

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Full': [
            ['SpellChecker', 'Scayt', 'Image', 'Flash',
                'Table', 'HorizontalRule', 'Smiley'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select'],            '/',        [
                'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink'],            '/',
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['ShowBlocks']

        ],
        'tabSpaces': 2,
        'width': '100%',
        'height': '100%',
        'toolbar': 'Full',  # 工具欄全部功能
        'extraPlugins': 'codesnippet',  # 插入程式code
    }
}

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

ROOT_URLCONF = 'MakerCenter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'Frontend', 'templates').replace("\\", '/'),
            os.path.join(BASE_DIR, 'Backend', 'templates').replace("\\", '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MakerCenter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True

USE_L10N = False
DATE_FORMAT = "Y/m/d"
DATETIME_FORMAT = "Y/m/d H:i:s"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# 建立自己新的靜態資料夾
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_ROOT = [os.path.join(BASE_DIR, "media")]

# scss setting
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]
SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static/scss'),
]
SASS_PROCESSOR_AUTO_INCLUDE = False
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
SASS_PRECISION = 8


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# # CSRF_COOKIE_HTTPONLY = True
# if  DEBUG :
#     # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#     # SESSION_COOKIE_SECURE = False
# #    SECURE_SSL_REDIRECT = False
# else:
#     # SECURE_BROWSER_XSS_FILTER = True
#     # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#  #   SECURE_SSL_REDIRECT = True
#     # SESSION_COOKIE_SECURE = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
