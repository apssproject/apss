import sys
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()


setup(
   name='apss',
   version='1.0.beta-1',
   description='Air Pollution Scanning System',
   license="GPLv3",
   long_description=long_description,
   author='APSS project',
   author_email='project.apss.system@gmail.com',
   url="http://www.a-pss.com/",
   packages=['apss'],
   install_requires=['PyGObject'],
)
