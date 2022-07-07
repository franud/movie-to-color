from fileinput import filename
import sys
import cv2
import numpy as np
import os

FRAMES_PER_SECOND = 1

def usage (argv):
    if len(argv) != 2:
        error_msg = '''Usage: python3 video_to_colors.py path_to_video'''
        print(error_msg, file=sys.stderr)
        exit(1)

def average_color (frame):
    print (type (frame), frame)
    print ("\n\n\n")

def extract_average_photo (path) -> str:
    # filename = "/home/cpt/Documents/programming-projects/movie-to-color/alice.avi"
    filename = path
    video_capture = cv2.VideoCapture(filename)
    frame_count = 0
    image_count = 0
    
    while True:
        ret, frame = video_capture.read()
        if ret == False:
            break
        if frame_count % 25 == 0:
            average_color (frame) 
            image_count = image_count + 1
        frame_count = frame_count + 1
    
    return True


def main (argv):
    usage (argv)
    path = extract_average_photo(argv[1])


if __name__ == '__main__':
    main (sys.argv)
