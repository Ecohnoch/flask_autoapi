# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : setup.py
# @Function : TODO

#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='flask_auto_api',
    version='v1.0.0',
    description=(
        'Provide non-intrusive and one-click machine learning api release tool.'
    ),
    long_description=open('README.rst', encoding='utf8').read(),
    author='Ecohnoch',
    author_email='chuyuan@ruc.edu.cn',
    maintainer='Ecohnoch',
    maintainer_email='chuyuan@ruc.edu.cn',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Ecohnoch/flask_autoapi',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)