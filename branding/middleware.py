#!/usr/bin/env python
# -*- coding:  utf-8 -*-

from logging import getLogger

import settings as bsettings

logger = getLogger('branding')


class BrandingMiddleware(object):
    """Brand response headers
    """

    def process_response(self, request, response):
        """Add custom headers
        """

        for key, value in bsettings.BRANDIND:
            response[key] = value

        if bsettings.programming:
            response['X-Programming'] = programming

        if bsettings.server:
            response['Server'] = server

        if bsettings.site_name:
            response['X-Powered-By'] = site_name

        if bsettings.version:
            response['X-Version'] = version

        if bsettings.revision:
            response['X-Revision'] = revision

        return response


