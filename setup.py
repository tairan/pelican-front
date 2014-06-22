#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pelican_front import __version__


setup(
  name = "PelicanFront",
  version = __version__,

  install_requires = ['pelican==3.3'],

  author = "Tairan Wang",
  author_email = "tairan.wang@gmail.com",
)
