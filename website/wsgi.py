#from website import settings
#from api.base import settings as api_settings

#if not settings.DEBUG_MODE:
#    #from gevent import monkey
#    #monkey.patch_all()
#    # PATCH: avoid deadlock on getaddrinfo, this patch is necessary while waiting for
#    # the final gevent 1.1 release (https://github.com/gevent/gevent/issues/349)
#    # unicode('foo').encode('idna')  # noqa
#
#    from psycogreen.gevent import patch_psycopg  # noqa
#    patch_psycopg()


import os  # noqa
#from django.core.wsgi import get_wsgi_application  # noqa


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.base.settings')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.base.settings'
from website.app import init_app
#import six
#import sys
#from rest_framework.fields import Field
#from rest_framework.request import Request

#@property
#def context(self):
#    return getattr(self.root, '_context', {})
#
#
## Overriding __getattribute__ is super slow
#def __getattr__(self, attr):
#    try:
#        return getattr(self._request, attr)
#    except AttributeError:
#        info = sys.exc_info()
#        six.reraise(info[0], info[1], info[2].tb_next)
#
#Field.context = context
#Request.__getattr__ = __getattr__
#Request.__getattribute__ = object.__getattribute__


application = init_app()
#application = get_wsgi_application()

