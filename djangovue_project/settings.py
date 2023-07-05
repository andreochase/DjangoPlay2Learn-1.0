import os
from pathlib import Path
from django.urls import reverse_lazy


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-vtp&i1q!0^3tiq#b4nfhfb)rb1alfr4kdi@s(0w)!$==ju*-*g'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [
    # Installed by Django
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Third-party apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',

    # Local Apps
    'contact.apps.ContactConfig',
    'games.apps.GamesConfig',
    'users.apps.UsersConfig',
    'review.apps.ReviewConfig',
]

SITE_ID = 1 

#ACCOUNT_EMAIL_REQUIRED = True  See AUTHENTICATION SETTINGS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangovue_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'libraries':{
                'common_filters': 'common.templatetags.common_filters',
                }
        },
    },
]

WSGI_APPLICATION = 'djangovue_project.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = 'chase.andreho@gmail.com'
CONTACT_EMAIL = 'chase.andreho@gmail.com'
ADMIN_EMAILS = 'chase.andreho@gmail.com'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


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


AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = reverse_lazy('account:login')
LOGIN_REDIRECT_URL = 'games:homepage'


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_EMAIL_VERIFICATION = 'optional' 
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
#LOGOUT_REDIRECT_URL = reverse_lazy('account:logout')
ACCOUNT_LOGIN_REDIRECT_URL = reverse_lazy('games:homepage')
ACCOUNT_USERNAME_REQUIRED = True 


ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.AllowAllUsersModelBackend', )


if os.environ.get('ENVIRONMENT') != 'production':
    from .local_settings import *
