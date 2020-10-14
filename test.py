import function1 as f1
import cv2
import adb_name
from baidulib.ocr import *
from baidulib.img_search import *
import returnhome as rh
import settings
b = settings.Buttons()
sb = settings.ShopButtons()

list1 = []

def check_credict():
    icon = f1.get_screen()
    icon = icon[b.cred_y[0]: b.cred_y[1], b.cred_x[0]: b.cred_x[1]]
    cv2.imwrite('icon_buffer/cred_num.png', icon)
    num = img_to_str('icon_buffer/cred_num.png')
    print('credit number is', num)

    while num >= '200':
        return True
    else:
        return False

def taglists():
    print('信用商店商品分析中...')
    mat = f1.get_screen()
    for i in range(0, 10):
        tag = mat[sb.shoptag[i][1][0]: sb.shoptag[i][1][1], sb.shoptag[i][0][0]: sb.shoptag[i][0][1]]
        cv2.imwrite('icon_buffer/shoptag_%d.png'%i, tag)

def tagimg2str():

    for i in range(0, 10):
        list1.append(img_to_str('icon_buffer/shoptag_%d.png'%i))
    print(list1)

def buy():
    g = 0
    print('开始购买...')
    print(set(sb.buylist))
    print(check_credict())
    while g < len(list1):
        if list1[g] in set(sb.buylist) and (check_credict()== True):
            f1.taptapl(f1.random_tapl(sb.shoptag[g]))
        else:
            break


if __name__ == '__main__':
    taglists()
    tagimg2str()
    buy()
