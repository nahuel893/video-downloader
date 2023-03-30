import yt_dlp as dl
import os

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
    def download(self, link=''):

        # Hook para recibir datos de progreso de yt-dlp
        def my_hook(d):
            if d['status'] == 'downloading':
                self.dMbytes = d['downloaded_bytes']
                self.percent = self.__clean_percent(d['_percent_str'])
                file = open('./percent.txt', 'a')
                file.write(self.percent + '\n')
                file.close()
            elif d['status'] == 'finished':
                self.status = 'finished'


        opts = {
            'progress_hooks': [my_hook],
        }
        with dl.YoutubeDL(opts) as ytdl:
            ytdl.download([link])
            os.remove('percent.txt')
            file = open('percent.txt', 'a')
            file.close()


if __name__ == '__main__':
    d = Downloader()
    d.download(
        'https://www.youtube.com/watch?v=3YP_KHgVMa4&ab_channel=LinuxZone')
