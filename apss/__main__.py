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

import os
import sys
import argparse

from apss.interface import gui


def main():
    """ First entry of the program.
        This function check sys.argv array and parse
        the program in right execution.
    """
    # If current working directory is in subdir /apss/apss
    # change it into his updir.
    if '/apss/apss' in os.path.dirname(os.path.realpath(__file__)):
        os.chdir(os.path.dirname(os.path.realpath(__file__))[:-5])

    # Starting checking sys.argv
    my_parser = argparse.ArgumentParser(description='List the content of a folder')

    # Declaration of script's options
    my_parser.add_argument('-r', '--readme', help='Print apss readme.', action="store_true")
    my_parser.add_argument('-v', '--version', help='Get current apss version.', action="store_true")
    my_parser.add_argument('-c', '--config', help='Open apss config file.', action="store_true")
    args = my_parser.parse_args()

    # Start parsing
    if args.readme:
        os.system("cat README")
    elif args.version:
        print(__version__)
    elif args.config:
        #os.system("")
        pass
    else:
        gui.start()


if __name__ == '__main__':
    main()
