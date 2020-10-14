from aip import AipImageSearch

config = {
    'appId': '22570794',
    'apiKey': 'w97dfwmVaGoWyWAbMbp5BUzz',
    'secretKey': 'wa4qHy5j9xcrzpScyktnv0i0nwatqWw7'
}

client = AipImageSearch(**config)

# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def image_add_to_lib(file_path):
    image = get_file_content(file_path)
    brief = {"name": "operators", "id": "003"}
    client.sameHqAdd(image, brief)

def image_search(img):
    image = get_file_content(img)
    result = client.sameHqSearch(image)

    print(result)
    return result
    # else:
    #     print('Warning: disable to read the input.\n')


# if __name__ == "__main__":
    # path ='D:/BaiduNetdiskDownload/emulator/nemu/vmonitor/bin/AUTOARK/icon/back/backbar.png'
    # img=get_file_content(path)
    # image_search(path)
#image_add_to_lib('path')


# def image_search(image_path):
#     image = get_file_content(image_path)
#     #输入用户本地图片作为检测模板
#     client.sameHqSearch(image)
#     #被检测图片
#     client.similarSearch(image)


