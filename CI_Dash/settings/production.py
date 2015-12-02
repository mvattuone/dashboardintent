from common import *

DEBUG = False
ALLOWED_HOSTS = ['dashboardintent.herokuapp.com']

# Parse database configuration from $DATABASE_URL
DATABASES = {'default': dj_database_url.config(
             default=os.environ['DATABASE_URL'])}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'