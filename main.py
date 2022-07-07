import sys
import cv2
import numpy as np
import os

FRAMES_PER_SECOND = 1

def usage (argv):
    if len(argv) != 2:
        error_msg = '''
        Usage: python3 video_to_colors.py path_to_video
        '''
        print(error_msg, file=sys.stderr)
        exit(1)

def extract_average_photo (path_to_video: str) -> str:
    video_capture = cv2.VideoCapture(path_to_video)
    fps = video_capture.get(cv.CAP_PROP_FPS)
    print (fps)


def main (argv):
    usage (argv)
    path = extract_average_photo(str)


if __name__ == '__main__':
    main (sys.argv)

