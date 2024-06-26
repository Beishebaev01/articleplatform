"""
settings.py - Это файл настроек Django,
который содержит все настройки проекта.

Приложение (app) - это набор функций,
которые работают вместе для выполнения определенной задачи.

127.0.0.1:8000 - это локальный адрес, который используется для тестирования проекта.
"""
from pathlib import Path

# BASE_DIR - это путь к каталогу проекта Django.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - это секретный ключ Django, для безопасности проекта.
SECRET_KEY = 'django-insecure-2nbmfvs*#6a=rtv3!d549c$yvid6%=(c_4mul$ch)t-=vqun5e'

# DEBUG - это переменная, которая включает или отключает режим отладки.
DEBUG = True

# ALLOWED_HOSTS - это список доменов, которые могут обслуживаться этим проектом.
ALLOWED_HOSTS = []


# INSTALLED_APPS - это список всех приложений, которые установлены в проекте Django.
INSTALLED_APPS = [
    'django.contrib.admin',  # Приложение администратора Django.
    'django.contrib.auth',  # Приложение аутентификации Django.
    'django.contrib.contenttypes',  # Приложение типов контента Django.
    'django.contrib.sessions',  # Приложение сессий Django.
    'django.contrib.messages',  # Приложение сообщений Django.
    'django.contrib.staticfiles',  # Приложение статических файлов Django.

    # Third-party apps


    # Custom apps
    'article',
    'user'
]

# MIDDLEWARE - это список всех промежуточных программ, которые используются в проекте Django.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Промежуточная программа безопасности Django.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Промежуточная программа сессий Django.
    'django.middleware.common.CommonMiddleware',  # Промежуточная программа общего доступа Django.
    'django.middleware.csrf.CsrfViewMiddleware',  # Промежуточная программа CSRF Django.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Промежуточная программа аутентификации Django.
    'django.contrib.messages.middleware.MessageMiddleware',   # Промежуточная программа сообщений Django.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Промежуточная программа XFrameOptions Django.
]

# ROOT_URLCONF - это корневой URL-адрес проекта Django.
ROOT_URLCONF = 'articleplatform.urls'

# TEMPLATES - это список всех шаблонов, которые используются в проекте Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'  # Каталог шаблонов Django.
        ],   # Каталоги шаблонов Django.
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

# WSGI_APPLICATION - это приложение WSGI, которое используется в проекте Django.
WSGI_APPLICATION = 'articleplatform.wsgi.application'

# DATABASES - это список всех баз данных, которые используются в проекте Django.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# AUTH_PASSWORD_VALIDATORS - это список всех валидаторов паролей, которые используются в проекте Django.
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


# LANGUAGE_CODE - это язык, который используется в проекте Django.
LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE - это часовой пояс, который используется в проекте Django.
TIME_ZONE = 'Asia/Bishkek'

# USE_I18N - это переменная, которая включает или отключает интернационализацию.
USE_I18N = True

# USE_TZ - это переменная, которая включает или отключает использование часовых поясов
USE_TZ = True

# STATIC_URL - это URL-адрес статических файлов, который используется в проекте Django.
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT_AUTO_FIELD - это поле по умолчанию для моделей Django.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
