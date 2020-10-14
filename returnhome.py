import os
import function1 as f1
from baidulib.img_search import *
import settings
import adb_name
import cv2

b = settings.Buttons()
sb = settings.ShopButtons()

def Tapreturn():

    x0 = b.tapreturn_x
    y0 = b.tapreturn_y

    cmd_back = '{str1} shell input tap {x1} {y1}'.format(
        str1=adb_name.adbname(),
        x1=x0,
        y1=y0
    )
    #print(cmd_back)
    os.system(cmd_back)

def back2home():
    home = check_is_home()
    while home == False:
        Tapreturn()
        f1.wait_time(2, 3)
        home = check_is_home()

def check_is_home():
    icon = f1.get_screen()
    #剪裁齿轮位置
    cut_icon = icon[b.gear_x[0]: b.gear_x[1], b.gear_y[0]: b.gear_y[1]]
    #缓存到本地（待优化）
    cv2.imwrite('icon_buffer/cut_icon.png', cut_icon)

    result = image_search('icon_buffer/cut_icon.png')

    for item in result['result']:
        if item['brief'] == 'gear':
            return True
        else:
            return False



if __name__ == '__main__':
    back2home()








