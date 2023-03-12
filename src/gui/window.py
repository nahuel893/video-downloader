# import gi
# gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys
sys.path.insert(0, '../downloader')
from downloader.download import Downloader 
sys.path.insert(0, '../db')
from db.database import Data


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        self.display_download()
        self.display_history()

    def run(self):
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def display_download(self):
        self.download_page = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=6)
        self.set_default_size(300, 300)

        self.download_label = Gtk.Label(label="Paste the link of video")
        self.download_page.pack_start(self.download_label, False, False, 0)

        self.download_entry = Gtk.Entry()
        self.download_page.pack_start(self.download_entry, False, False, 0)

        self.download_button = Gtk.Button(label="Download")
        self.download_button.connect("clicked", self.__on_button_clicked)
        self.download_page.pack_start(self.download_button, False, False, 0)

        self.notebook.append_page(self.download_page,
                                  Gtk.Label(label='Download'))

    def __on_button_clicked(self, widget):
        link = self.download_entry.get_text()
        d = Downloader()
        d.download(link)
        self.data.insert(link)

        if d.status == 'finished':
            print('status is finished')
            self.update_history()

    def display_history(self):
        # History page
        self.history_page = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=6)

        # Model
        self.store = Gtk.ListStore(str, str)
        self.data = Data()
        self.data.create_connection()
        regist = self.data.select()

        for row in regist:
            self.store.append([row[1], row[2]])

        # View, set columns respect data inserted
        self.view = Gtk.TreeView(model=self.store)
        column1 = Gtk.TreeViewColumn(
            'Source', Gtk.CellRendererText(), text=0, weight=1)

        column2 = Gtk.TreeViewColumn(
            'Date', Gtk.CellRendererText(), text=1, weight=1)

        self.view.append_column(column1)
        self.view.append_column(column2)

        # Put in the notebook
        self.history_page.pack_start(self.view, False, False, 0)
        self.notebook.append_page(self.history_page,
                                  Gtk.Label(label='History'))

    # Add the last input of DB
    def update_history(self):
        self.data.create_connection()
        regist = self.data.select()
        print(regist)
        last = regist[len(regist)-1]
        self.store.append([last[1], last[2]])


if __name__ == '__main__':
    win = MyWindow()
    win.run()
