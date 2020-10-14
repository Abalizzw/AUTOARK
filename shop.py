import os
import time
import cv2
from baidulib.ocr import *
import settings
from function1 import *
import returnhome as rh

sb = settings.ShopButtons()
b = settings.Buttons()

#进入商店
def enter_shop():
    x1, y1 = random_tap(b.shop_x, b.shop_y)
    taptap(x1, y1)
    wait_time(3, 4)
    taptap(1340, 116)
    wait_time(3, 4)

#检查剩余信用，大于200，输出True
def check_credict():
    icon = get_screen()
    icon = icon[b.cred_y[0]: b.cred_y[1], b.cred_x[0]: b.cred_x[1]]
    cv2.imwrite('icon_buffer/cred_num.png', icon)
    num = img_to_str('icon_buffer/cred_num.png')

    while num >= '200':
        return True
    else:
        return False

#存储十个tag
def taglists():
    ilist = []
    mat = get_screen()
    for i in range(0, 9):
        tag = mat[sb.shoptag[i][1][0]: sb.shoptag[i][1][1], sb.shoptag[i][0][0]: sb.shoptag[i][0][1]]
        cv2.imwrite('icon_buffer/shoptag_%d.png'%i, tag)

#识别商品名转字符
def tagimg2str():
    list1 = []
    for i in range(0, 9):
        list1.append(img_to_str('icon_buffer/shoptag_%d.png'%i))
    print(list1)



if __name__ == '__main__':

    #返回主界面
    rh.back2home()
    wait_time(3, 4)

    #进入商店
    enter_shop()

    #点击信用收取按钮2次
    taptap(1150, 43)
    wait_time(1, 2)
    taptap(1150, 43)








