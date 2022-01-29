#!/usr/bin/env python

from setuptools import setup

setup(
    name='fetchmseval',
    version='0.1.0',
    author="Chris Grieger",
    author_email="chris@grieger.biz",
    url="https://github.com/fourcube/fetchmseval",
    packages=['fetchmseval'],
    install_requires=[
        'requests==2.27.1',
        'bs4==4.10.0',
        'tabulate==0.8.9',
        'tqdm==4.52.3'
    ],
)
