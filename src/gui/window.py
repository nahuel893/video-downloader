from downloader.download import Downloader
import gi
from logger.logger import MyLogger
# from multiprocessing import Process
from db.database import Data
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


_logger = MyLogger(__name__)


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Downloader")
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Init conection with database
        self.data = Data()
        self.data.create_connection()

        # Display page of window
        self.display_download()
        self.display_history()

        self.link = ''

        # A flag for daemon thread while loop stop
        self.flag_daemon = True

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

        # Display progress bar
        self.progress_bar = Gtk.ProgressBar(show_text=True)
        self.progress_bar.set_fraction(0.0)
        self.download_page.pack_start(self.progress_bar, False, False, 0)

        self.notebook.append_page(self.download_page,
                                  Gtk.Label(label='Download'))

    def update_progress(self, fraction, bytes_downloaded, video_size):
        self.progress_bar.set_fraction(fraction)
        self.progress_bar.set_text("{:.0%}".format(fraction))
        self.progress_bar.set_tooltip_text(
                "{}/{}".format(bytes_downloaded, video_size))

    def __on_button_clicked(self, widget):
        # Process for download
        link = self.download_entry.get_text()

        if link != "":
            self.progress_bar.set_fraction(0)
            downloader = Downloader()
            downloader.run(self.update_progress)

        # Insert data in db
        self.data.insert(self.link)
        if downloader.status == 'finished':
            self.update_history()

    def display_history(self):
        # Create History page
        self.history_page = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=6)

        # Model
        self.store = Gtk.ListStore(str, str)
        regist = self.data.select()
        for row in regist:
            self.store.append([row[1], row[2]])

        # View
        self.view = Gtk.TreeView(model=self.store)

        # Set columns respect data inserted
        # text=0 first column, text=1 second column
        column1 = Gtk.TreeViewColumn(
            'Source', Gtk.CellRendererText(), text=0)
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
        regist = self.data.select()
        # print(regist)
        last = regist[len(regist)-1]
        self.store.append([last[1], last[2]])


if __name__ == '__main__':
    win = MyWindow()
    win.run()
