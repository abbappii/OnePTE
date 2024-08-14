from __future__ import absolute_import, unicode_literals
import os
import logging
import dotenv
from celery import Celery
from django.conf import settings

logger = logging.getLogger(__name__)

# Load env vars from .env
dotenv.read_dotenv()
# set the default Django settings module for the 'celery' program.
DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE', 'OnePTE.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

app = Celery('OnePTE')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

