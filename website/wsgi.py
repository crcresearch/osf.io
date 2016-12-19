import os

from website.app import init_app
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.base.settings'
application = init_app()
