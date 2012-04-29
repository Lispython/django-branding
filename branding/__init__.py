#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
django-branding
~~~~~~~~~~~~~~~
"""

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('branding').version
except Exception, e:
    VERSION = 'unknown'
