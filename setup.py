#!/usr/bin/env python

from setuptools import setup, find_packages

DESCRIPTION = ("Simple Twitch Chat Wrapper written in Python")
LONG_DESCRIPTION = open('README.rst').read()
VERSION = __import__('twitch_chat_wrapper').__version__

setup(
    name='twitch_chat_wrapper',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Arthur Barros',
    author_email='arthbarros@gmail.com',
    url='https://github.com/arthurbarros/twitch-chat-wrapper',
    license=open('LICENSE').read(),
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'events'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
)
