import os
import cv2
import function1 as f1
from settings import Settings

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def match_main():
    #background
    tb = f1.get_screen()
    #template
    tt = cv2.imread('icon/main/gear.png', 0)
    f1.match(tb, tt)
