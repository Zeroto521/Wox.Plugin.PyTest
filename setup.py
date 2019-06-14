# -*- coding: utf-8 -*-

from __future__ import print_function

import os

from setuptools import find_packages, setup

NAME = "pytest"
GITHUB_USERNAME = "Zeroto521"

try:
    # GitHub Short Description
    SHORT_DESCRIPTION = __import__(NAME).__short_description__
except:
    print("'__short_description__' not found in '%s.__init__.py'!" % NAME)
    SHORT_DESCRIPTION = "No short description!"

try:
    LONG_DESCRIPTION = open("README.md", "r").read()
except:
    LONG_DESCRIPTION = "No long description!"

VERSION = __import__(NAME).__version__
AUTHOR = "Zero"
AUTHOR_EMAIL = "Zeroto521@gmail.com"
MAINTAINER = "Zero"
MAINTAINER_EMAIL = "Zeroto521@gmail.com"

repository_name = os.path.basename(os.getcwd())
URL = "https://github.com/{}/{}".format(GITHUB_USERNAME, repository_name)
DOWNLOAD_URL = "https://github.com/{}/{}/archive/master.zip".format(
    GITHUB_USERNAME, repository_name)

try:
    LICENSE = __import__(NAME).__license__
except:
    print("'__license__' not found in '%s.__init__.py'!" % NAME)
    LICENSE = ""

PLATFORMS = ["Windows", "MacOS", "Unix"]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",

    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Natural Language :: English",
    "Natural Language :: Chinese (Simplified)",

    "Operating System :: Microsoft :: Windows",

    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",

    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules'
]


setup(
    name=NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    packages=find_packages(),
    include_package_data=True,
    url=URL,
    download_url=DOWNLOAD_URL,
    platforms=PLATFORMS,
    license=LICENSE
)
