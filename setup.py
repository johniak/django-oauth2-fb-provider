#!/usr/bin/env python

from setuptools import setup, find_packages
import provider

setup(
    name='django-oauth2-fb-provider',
    version=provider.__version__,
    description='Provide OAuth2 access to your app, and auth',
    long_description=open('README.md').read(),
    author='Jan Romaniak',
    author_email='romaniakjan@gmail.com',
    url='https://github.com/johniak/django-oauth2-fb-provider',
    packages=find_packages(exclude=('tests*',)),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        "shortuuid>=0.3",
        "python-social-auth>=0.1.26"
    ],
    include_package_data=True,
    zip_safe=False,
)
