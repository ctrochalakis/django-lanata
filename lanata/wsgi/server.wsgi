import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'lanata.settings'
this_dir = os.path.abspath(os.path.dirname(__file__))
top_dir = os.path.split(this_dir)[0]
sys.path.append(top_dir)
from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
