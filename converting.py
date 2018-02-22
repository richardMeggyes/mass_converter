import ui
import os

def get_video_data(video_file):
    width = ""
    frames = ""
    for line in os.popen('mediainfo --fullscan "{}"'.format(video_file)).readlines():
        if "Frame count" in line:
            frames = int(line.split(":")[1].strip())
        if "Width" in line:
            width = int(line.split(":")[1].strip())
            break

    ui.print_debug_message("Width: {}, Frames: {}".format(width, frames))
    return width, frames

def convert_files(video_list):
    for input_file in video_list:
        ui.print_info("Getting info for file: {}".format(input_file))
        width, frames = get_video_data(input_file)

        if type(width) == str or type(frames) == str:
            ui.print_error_message("ERROR: Could not get data from video file. Skipping file. Width: {} frames: {}".format(width, frames))
