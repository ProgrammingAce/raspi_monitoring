import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.core import management
management.call_command('syncdb', interactive=False)
