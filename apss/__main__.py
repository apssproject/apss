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

from interface.gui import gui

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)


def print_help():
    """ Print apss help using sys.stderr.write """
    sys.stderr.write("""apss """ + __version__ + """
usage: apss [--version/-v] [--help/-h]
            [--readme/-r] [--config/-c]
""")


def main():

    if len(sys.argv) < 2:
            gui.start()
    else:

        if '--readme' in sys.argv or '-r' in sys.argv:
            os.system("cat README.*")

        elif '--version' in sys.argv or '-v' in sys.argv:
            print(__version__)

        elif '--help' in sys.argv or '-h' in sys.argv:
            print_help()

        elif '--config' in sys.argv or '-c' in sys.argv:
            # os.system("apss\\Data\\json\\Settings.json")
            pass

        else:
            print("Wrong syntax.\napss --help")
            print_help()


if __name__ == '__main__':
    main()
