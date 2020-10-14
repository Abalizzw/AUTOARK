import os
import cv2
import random
import time
import adb_name

def get_screen():
    #截屏口令
    cmd_get = '{str1} shell screencap -p /sdcard/screen_img.png'.format(
        str1=adb_name.adbname()
    )
    #发送图片口令
    cmd_send = '{str1} pull /sdcard/screen_img.png screen/screen_img.png'.format(
        str1=adb_name.adbname()
    )
    #cmd_get='adb_server exec-out screencap -p > screen/screen.png'
    #截屏和发送操作
    os.system(cmd_get)
    os.system(cmd_send)
    img = cv2.imread('screen/screen_img.png', 0)
    return img

def taptap(x, y):

    cmd_back = '{str1} shell input tap {x1} {y1}'.format(
        str1=adb_name.adbname(),
        x1=x,
        y1=y
    )
    print(cmd_back)
    os.system(cmd_back)

def taptapl(list):

    cmd_back = '{str1} shell input tap {x1} {y1}'.format(
        str1=adb_name.adbname(),
        x1=list[0],
        y1=list[1]
    )
    #print(cmd_back)
    os.system(cmd_back)

def match(img1, template):
    """img1代表待匹配图像, img2代表模板"""
    res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)
    res_max = res.max()

    return res_max

def wait_time(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))


def random_tap(x, y):
    """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
    xc = random.randint(x[0], x[1])
    yc = random.randint(y[0], y[1])

    return xc, yc

def random_tapl(list):
    """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
    list_random = []
    list_random[0] = random.randint(list[0][0], list[0][1])
    list_random[1] = random.randint(list[1][0], list[1][1])

    return list_random
