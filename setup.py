#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# Dynamically calculate the version based on photologue.VERSION
version_tuple = __import__('photologue').VERSION
if len(version_tuple) == 3:
    version = "%d.%d.%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

install_requires = [
    'Django>=1.4',
    'PIL',
    'django-taggit',
]

setup(
    name = "django-photologue",
    version = version,
    description = "Powerful image management for the Django web framework.",
    author = "Optim Informatique",
    author_email = "mcordoquy@optiminformatique.fr",
    url = "http://github.com/mcordoquy/django-photologue",
    packages = find_packages(),
    package_data = {
        'photologue': [
            'res/*.jpg',
            'locale/*/LC_MESSAGES/*',
            'templates/photologue/*.html',
            'templates/photologue/tags/*.html',
        ]
    },
    zip_safe = False,
    test_suite="setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.0.6',
    ],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
