

import os
import sys

path = '/home/bondaditya/simuli'

if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application

from django.contrib.staticfiles.handlers import StaticFilesHandler

from django.contrib.staticfiles.handlers import StaticFilesHandler 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simuli.settings")

application = StaticFilesHandler(get_wsgi_application())
