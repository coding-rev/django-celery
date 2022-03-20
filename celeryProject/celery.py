from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryProject.settings')

app = Celery('celeryProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# If you have an existing Django project, you can now create a file called tasks.py inside any app. Celery will automatically detect that file and look for worker tasks you define there.
# For simplicity, though, we’re going to create our first task in celery_tutorial/celery.py , so re-open that file and add this to the bottom:
@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))