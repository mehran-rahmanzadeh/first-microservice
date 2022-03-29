import os
from datetime import timedelta

from decouple import config
from django.conf import settings

from .base import (
    INSTALLED_APPS, MIDDLEWARE,
    STATIC_ROOT, BASE_DIR, STATICFILES_DIRS
)

# ############## #
#   EXTENSIONS   #
# ############## #

# admin
INSTALLED_APPS.append('django.contrib.admindocs')
INSTALLED_APPS.append('django.contrib.sites')

# packages
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('corsheaders')
INSTALLED_APPS.append('admin_footer')
INSTALLED_APPS.append('admin_honeypot')
INSTALLED_APPS.append('cachalot')
INSTALLED_APPS.append('rest_framework_simplejwt')
INSTALLED_APPS.append('django_grpc_framework')

# Log
INSTALLED_APPS.append('django_admin_logs')
INSTALLED_APPS.append('simple_history')
MIDDLEWARE.append('simple_history.middleware.HistoryRequestMiddleware')
INSTALLED_APPS.append('request')
MIDDLEWARE.append('request.middleware.RequestMiddleware')
INSTALLED_APPS.insert(0, 'postgres_metrics.apps.PostgresMetrics')

# Security
INSTALLED_APPS.append('defender')
MIDDLEWARE.append('defender.middleware.FailedLoginMiddleware')

# Applications
INSTALLED_APPS.append('drf_yasg')
INSTALLED_APPS.append('users')

# ###################### #
#     REST FRAMEWORK     #
# ###################### #

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '30/minute'
    # },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS512',
    'VERIFYING_KEY': None,
    'AUDIENCE': 'ShoppingCenter',
    'ISSUER': 'User',

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# #################### #
#   BACKGROUND TASKS   #
# #################### #
# BACKGROUND_TASK_RUN_ASYNC = True

# ########### #
#   CELERY    #
# ########### #
# CELERY_BROKER_URL = config('CELERY_BROKER_URL')
# CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_TASK_ROUTES = {
#     'analysis.tasks.process_nmea_report_file': {'queue': 'gps_process'},
#     'authentication.tasks.send_mail': {'queue': 'email'}
# }
# CELERY_ENABLE_UTC = True
# CELERY_TIMEZONE = 'UTC'

# ########## #
#   CACHE    #
# ########## #
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('REDIS_HOST')
    }
}
CACHE_TIMEOUT = 3600

# ########### #
#   UPLOAD    #
# ########### #
# FILE_UPLOAD_HANDLERS = [
#     'painless.utils.handlers.upload.ChunkFileUploadHandler'
# ]
# UPLOAD_CHUNK_SIZE = 2500 * 2 ** 10  # 2500 KB

# ######################### #
#       AdminInterface      #
# ######################### #
from datetime import datetime

ADMIN_FOOTER_DATA = {
    'site_url': 'https://google.com',
    'site_name': 'Google',
    'period': '{}'.format(datetime.now().year),
    'version': 'v1.0.0 - production'
}

# #################### #
# IMPORTANT VARIABLES  #
# #################### #

# LOGIN_REDIRECT_URL = '/portal'
# LOGIN_URL = '/auth/login'
# LOGOUT_REDIRECT_URL = '/'
# AUTH_USER_MODEL = 'users.User'

# ############### #
# LOCATION FIELD  #
# ############### #
# MAPBOX_KEY = "pk.eyJ1IjoibXJobnoiLCJhIjoiY2txMjRldDFnMDBuNjJ1b250dWVwaGJ1eSJ9.bShZpSW_qEyIZF_Qvnbhnw"

# ############  #
#    TWILIO     #
# ############  #
# AUTHY_API_KEY = config('AUTHY_API_KEY')

# ###########  #
#    TOKEN     #
# ###########  #
# EMAIL_FROM = 'test@gmail.com'

# ########################### #
#     DJANGO CORS HEADERS     #
# ########################### #
from corsheaders.defaults import default_headers
from corsheaders.defaults import default_methods

CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

# #################### #
#   Django Defender    #
# #################### #
DEFENDER_REDIS_NAME = "default"

# ################ #
#   User Agents    #
# ################ #
USER_AGENTS_CACHE = 'default'

# ################## #
#   Debug Toolbar    #
# ################## #
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
#
#
# def custom_show_toolbar(request):
#     return True
#
#
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
#     'INSERT_BEFORE': '</body>'
# }

# ######### #
#   Auth    #
# ######### #
# RESET_PASSWORD_TOKEN_TIMEOUT = 120  # s
# DEFAULT_FROM_EMAIL = 'mail@saqr.com'
AUTH_USER_MODEL = 'users.User'

CACHALOT_UNCACHABLE_APPS = ('admin', 'auth')