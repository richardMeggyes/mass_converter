import os, ui
from preferences import videoformats

def decide_if_file_is_video(path):
    if path[-3:].lower() in videoformats:
        return True
    return False

def get_video_files(path):
    video_list = []
    ui.print_info("Getting files list")
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file = os.path.join(root, name)
            if decide_if_file_is_video(file):
                video_list.append(file)
    ui.print_info("Found {} video files".format(len(video_list)))
    return video_list

def tagged_file_name(path):
    file_name = path[len(path) - 1]
    print(file_name)