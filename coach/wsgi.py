"""
WSGI config for coach project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coach.settings")

from django.core.wsgi import get_wsgi_application

# below was commented OUT to put onto Heroku ----------------------------------- ....

application = get_wsgi_application()

# ... and then this was added FOR HEROKU -----------------------------------....
#
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling
#
# application = Cling(get_wsgi_application())


