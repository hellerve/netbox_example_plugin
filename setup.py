#!/usr/bin/env python
import os
from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='netbox-example-plugin',
    author='Veit Heller',
    version='0.0.1',
    license='MIT',
    url='https://github.com/hellerve/netbox-example-plugin',
    description='A Netbox example plugin',
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url = 'https://github.com/hellerve/netbox-example-plugin/-/archive/0.0.1/netbox-example-plugin-0.0.1.tar.gz',
    packages=find_packages('.'),
    install_requires=[
    ],
)

