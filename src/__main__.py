#!/usr/bin/env python

"""__main__.py: Main entry of APSS.
"""

__author__ = "APSS project"
__email__ = "project.apss.system@gmail.com"
__license__ = "GPLv3"

import os
import sys

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

__version__ = 'v1.0.beta-1'


def PRINT_HELP():
    sys.stderr.write(__version__ + """\nusage: apss [--version] [--help]""")


def start_gui():
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    class Handler:
        def onDestroy(self, *args):
            Gtk.main_quit()

        def onButtonPressed1(self, button):
            print("Hello World!")

        def onButtonPressed2(self, button):
            print("Hello Worsdsdssld!")

        def onButtonPressed3(self, button):
            print("Hello Worldddddd!")


    builder = Gtk.Builder()
    builder.add_from_file("builder_example.glade")
    builder.connect_signals(Handler())

    window = builder.get_object("window1")
    window.show_all()

    Gtk.main()


def main():

    if len(sys.argv) < 2:
        start_gui()
    else:

        if '--readme' in sys.argv or '-r' in sys.argv:
            os.system("cat README.*")

        elif '--version' in sys.argv or '-v' in sys.argv:
            print(__version__)

        elif '--help' in sys.argv or '-h' in sys.argv:
            PRINT_HELP()

        elif '--config' in sys.argv or '-c' in sys.argv:
            # os.system("apss\\Data\\json\\Settings.json")
            pass

        else:
            print("Wrong syntax.")
            PRINT_HELP()


if __name__ == '__main__':
    main()
