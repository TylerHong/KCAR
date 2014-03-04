import os
import sys

sys.path.append('/home/ubuntu/PROJECT/kcar')
os.environ['DJANGO_SETTINGS_MODULE'] = 'kcar.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
