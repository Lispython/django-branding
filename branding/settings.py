#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from django.conf import settings

BRANDIND = getattr(settings, 'BRANDING', {})

# Variable type settings have priority

server = getattr(settings, "X_SERVER", "Branding Serv")
programming = getattr(settings, "X_PROGRAMMING", "Alexandr Lispython http://github.com/lispython/django-branding")
site_name = getattr(settings, "SITE_NAME")
version = getattr(settings, 'VERSION')
revision = getattr(settings, 'REVISION')
