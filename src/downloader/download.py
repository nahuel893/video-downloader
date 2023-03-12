import yt_dlp as dl


class Downloader:
    def __init__(self):
        self.status = ''

    def my_hook(self, d):
        if d['status'] == 'finished':
            self.status = 'finished'

    def download(self, link=''):
        opts = {
            'progress_hooks': [self.my_hook],
        }

        with dl.YoutubeDL(opts) as ytdl:
            ytdl.download([link])


if __name__ == '__main__':
    Downloader.download('https://fb.gg/v/i-_JRH03SN/')
