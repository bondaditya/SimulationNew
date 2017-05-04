 """
WSGI config for simuli project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/bondaditya/simuli'

if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simuli.settings")

application = StaticFilesHandler(get_wsgi_application())
