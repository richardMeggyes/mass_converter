import logging, time
import ui
import converting

from file_manager import *

if __name__ == "__main__":
    ui.print_info('Mass converter started')
    path = "e:/PycharmProjects/VIDEOS/"

    converting.convert_files(get_video_files(path))