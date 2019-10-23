from django.db import models

# Create your models here.

from django.conf import settings

from rest_framework.authtoken.models import Token as DefaultTokenModel

from repoApp.utils import import_callable

# Register your models here.

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))