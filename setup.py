#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################

from setuptools import setup, find_packages, Distribution

# class BinaryDistribution(Distribution):
#     def has_ext_modules(foo):
#         return True

setup(name="pipeg",
      version="0.0.1",
      packages=find_packages(),
      package_dir={'': '.'},
      package_data={'': ['arithmetic.cpython-36m-x86_64-linux-gnu.so']},
      include_package_data=True,
      platforms="any",
      install_requires=[])
