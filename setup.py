#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name='django_branding',
    version='0.0.6',
    author='Alexandr Lispython',
    author_email='alex@dzone.me',
    url='http://github.com/Lispython/django-branding',
    description='Add branding headers to you response',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'django',
    ],
    test_suite = 'branding.tests',
    include_package_data=True,
    cmdclass={"test": mytest},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
