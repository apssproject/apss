import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class gui:

    @staticmethod
    def start():

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
        builder.add_from_file("apss/resources/xml/builder_example.glade")
        builder.connect_signals(Handler())

        window = builder.get_object("window1")
        window.show_all()

        Gtk.main()
