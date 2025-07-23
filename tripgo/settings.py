from pathlib import Path
import os # ADDED: Import os module for path manipulation

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!g_bu&kv1^$n+%a@s*+kmp)vqycb$2vgz96k1a)ryb!71qio40'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website', # Your app is correctly listed here
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

ROOT_URLCONF = 'tripgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # MODIFIED: Tell Django where to find your project-wide templates.
        # Since 'index.html' is acting as your base, and it's inside website/templates,
        # we explicitly point to that directory.
        'DIRS': [os.path.join(BASE_DIR, 'website', 'templates')],
        'APP_DIRS': True, # Keep this so Django also looks for templates inside app's 'templates' folder (e.g., admin templates)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # ADDED: Useful debug context
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tripgo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/' # MODIFIED: Add leading slash for consistency and best practice
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'website', 'static') # MODIFIED: Use os.path.join for clarity and cross-OS compatibility
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # ADDED: Essential for `python manage.py collectstatic`

# MEDIA files configuration (for images uploaded via models, like Tour.image)
MEDIA_URL = '/media/' # ADDED: URL prefix for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # ADDED: Directory where uploaded media files will be stored

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication redirects (Crucial for login/logout flow)
LOGIN_REDIRECT_URL = 'home' # Where to redirect after successful login. 'home' is the name of your index URL.
LOGOUT_REDIRECT_URL = 'login' # Where to redirect after logout. 'login' is the name of your login URL.
LOGIN_URL = 'login' # The URL name for your login page. Used by @login_required decorator. 