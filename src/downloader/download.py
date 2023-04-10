import subprocess
from time import sleep
from gi.repository import GLib
from logger.logger import MyLogger

LINK = 'https://www.youtube.com/watch?v=3YP_KHgVMa4&ab_channel=LinuxZone'

_logger = MyLogger(__name__)


class Downloader():
    def __init__(self):
        self.status = ''

    def remove_empty_values(self, strings):
        return [string for string in strings if string != '']

    def string_contains_char(self, strings, char):
        for string in strings:
            if char in string:
                return string
        return ''

    def run(self, function_progress=None, link=LINK):
        command = f'''yt-dlp -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best -o "./%(title)s.%(ext)s" --no-warnings --newline {link}'''
        process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        video_size = 0

        while True:
            line = process.stdout.readline()
            if not line:
                break

            line = line.decode("utf-8").strip()
            _logger.info(line)

            if (
                    "[download]" in line
                    and "%" in line
                    and 'Destination' not in line
                    ):

                try:
                    strings_in_line = self.remove_empty_values(line.split(" "))
                    _logger.debug('var strings_in_line:' + str(strings_in_line))

                    progress_str = self.string_contains_char(strings_in_line, '%')
                    _logger.debug('var progress_str:' + progress_str)

                    fraction = float(progress_str[:-1]) / 100
                    _logger.debug('var fraction:' + str(fraction))
                except Exception as error:
                    _logger.error(f'var fraction: {fraction} - {error}')
                    raise SystemExit
                if not video_size:
                    try:
                        video_size_str = self.string_contains_char(strings_in_line, 'MiB')
                        _logger.debug(f'var video_size_str: {video_size_str}')

                        if video_size_str != '':
                            video_size = float(video_size_str[0:-3])
                            _logger.debug(f'var video_size:{video_size}')
                    except Exception as error:
                        _logger.error(f'var video_size:{video_size} - {error}')
                        raise SystemExit

                bytes_downloaded = float(fraction * video_size)
                _logger.debug(f'var bytes_downloaded: {bytes_downloaded}')

                if function_progress:
                    try:
                        GLib.idle_add(
                                function_progress,
                                fraction, bytes_downloaded,
                                video_size)
                    except Exception as error:
                        _logger.debug(error)


if __name__ == '__main__':
    d = Downloader()
    d.run()
