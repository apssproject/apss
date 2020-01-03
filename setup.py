#!/usr/bin/env python

"""
  apss - Air Pollution Scanning System
  Copyright (C) 2019 APSS project

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""__main__.py: Main entry of APSS.
"""

__author__ = "APSS project"
__email__ = "project.apss.system@gmail.com"
__license__ = "GPLv3"
__version__ = 'v1.0.beta-1'

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
