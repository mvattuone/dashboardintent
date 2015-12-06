from common import *

DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ['dashboardintent.herokuapp.com']

# Parse database configuration from $DATABASE_URL
DATABASES = {'default': dj_database_url.config(
             default=os.environ['DATABASE_URL'])}

