# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crowd4py',
    version='0.1.0',
    description='Crowd4u library for python',
    long_description=readme,
    author='Masafumi Hayashi',
    author_email='sshayashi0208@gmail.com',
    url='https://github.com/SShayashi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests', 'lxml']
)

