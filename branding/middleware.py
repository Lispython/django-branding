#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from logging import getLogger

from django.conf import settings

logger = getLogger('branding')


class BrandingMiddleware(object):
    """Brand response headers
    """

    def process_response(self, request, response):
        """Add custom headers
        """

        for key, value in getattr(settings, 'BRANDING', {}).iteritems():
            response[key] = value

        platform = getattr(settings, "PLATFORM", None)
        server = getattr(settings, "X_SERVER", None)
        programming = getattr(settings, "X_PROGRAMMING", None)
        site_name = getattr(settings, "SITE_NAME", None)
        version = getattr(settings, 'VERSION', None)
        revision = getattr(settings, 'REVISION', None)

        if programming:
            response['X-Programming'] = programming

        if server:
            response['Server'] = server

        if platform:
            response['Link'] = "<%s>; rel=\"platform\"" % platform

        if site_name:
            response['X-Powered-By'] = site_name

        if version:
            response['X-Version'] = version

        if revision:
            response['X-Revision'] = revision

        return response


