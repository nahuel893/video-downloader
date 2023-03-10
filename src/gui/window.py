# import gi
# gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys
sys.path.insert(0, '../downloader')
from downloader.download import Downloader 


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        self.set_default_size(300, 300)

        self.label = Gtk.Label(label="Paste the link of video")
        self.box.pack_start(self.label, False, False, 0)

        self.entry = Gtk.Entry()
        self.box.pack_start(self.entry, False, False, 0)

        self.button = Gtk.Button(label="Click Here")

        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, False, False, 0)

    def on_button_clicked(self, widget):
        link = self.entry.get_text()
        d = Downloader()
        print('LINK', link)
        d.download(str(link))

    def run(self):
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


if __name__ == '__main__':
    win = MyWindow()
    win.run()
