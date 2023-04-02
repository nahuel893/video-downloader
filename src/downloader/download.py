import yt_dlp as dl
# import os


LINK = 'https://www.youtube.com/watch?v=3YP_KHgVMa4&ab_channel=LinuxZone'


class Downloader:
    def __init__(self):
        self.status = ''
        self.dMbytes = None
        self.percent = None
        self.info = None

    # Clean percent value,
    def __clean_percent(self, percent):
        for i, char in enumerate(percent):
            if char == '%':
                value = percent[i-5:i+1].replace('%', '')
                break
        try:
            value = (float(value.replace(' ', '')) / 100)
        except Exception as e:
            print(e)

        return value

    # Hook para recibir datos de progreso de yt-dlp
    def my_hook(self, d):
        if d['status'] == 'downloading':
            self.dMbytes = d['downloaded_bytes']
            self.percent = self.__clean_percent(d['_percent_str'])
        elif d['status'] == 'finished':
            self.status = 'finished'

    def download(self, link=LINK):
        opts = {
            'progress_hooks': [self.my_hook],
        }
        with dl.YoutubeDL(opts) as ytdl:
            ytdl.download([link])


if __name__ == '__main__':
    d = Downloader()
    d.download()
