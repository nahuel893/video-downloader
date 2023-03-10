import yt_dlp as dl


class Downloader:
    def __init__(self):
        pass

    def download(self, link=''):
        opts = {}

        with dl.YoutubeDL(opts) as ytdl:
            ytdl.download([link])


if __name__ == '__main__':
    Downloader.download('https://fb.gg/v/i-_JRH03SN/')
