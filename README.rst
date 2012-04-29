django-branding
---------------

Add branding headers to response.


Requirements
============

* Django

Installation
============

Install it with pip (or easy_install)::

	pip install django-branding

Usage
=====

Add branding middleware from branding to you django config

     MIDDLEWARE_CLASSES += 'branding.middleware.BrandingMiddleware',

Define headers variables in settings

     BRANDING = {
         'X-Programming': 'Lispython',
         'X-Revision': '232134'
     }

     X_SERVER = "Super Server"


Example
=======

Example of headers on http://dzone.me


    In [1]: import human_curl as hurl

    In [2]: r = hurl.get('http://dzone.me')

    In [3]: r.headers
    Out[3]:
    {'cache-control': 'max-age=600',
    'connection': 'keep-alive',
    'content-language': 'ru-ru',
    'content-length': '55239',
    'content-type': 'text/html; charset=utf-8',
    'date': 'Sun, 29 Apr 2012 12:51:12 GMT',
    'expires': 'Sun, 29 Apr 2012 13:01:12 GMT',
    'last-modified': 'Sun, 29 Apr 2012 12:51:12 GMT',
    'link': '<dzone.me>; rel="platform"',
    'server': 'Super Server',
    'vary': 'Accept-Language, Cookie, Accept-Encoding',
    'x-powered-by': 'D Zone',
    'x-programming': 'Alex Lispython (alex@dzone.me, github.com/lispython)',
    'x-revision': '5215de3',
    'x-version': '20120311.0013-0'}
