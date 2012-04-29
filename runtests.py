#!/usr/bin/env python
import sys
from os.path import dirname, abspath
from optparse import OptionParser

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner


if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite',
                'NAME': 'branding_test',
            }
        },
        INSTALLED_APPS=[
            'branding',
            'branding.tests',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
    )



def runtests(*test_args):
    if not test_args:
        test_args = ['branding']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    interactive = '--no-input' not in sys.argv
    failures = DjangoTestSuiteRunner().run_tests(test_args, verbosity=1,
                                                 interactive=interactive)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)
