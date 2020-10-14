from aip import AipOcr

# 新建一个AipOcr对象
config = {
    'appId': '22570765',
    'apiKey': 'pLTR9WN6Tdlc8RN4BLrWnGxf',
    'secretKey': '7jTGtd0gsa9GGltMKD7h3c7GRvRxNSMQ'
}
client = AipOcr(**config)


# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

# 识别图片里的文字
def img_to_str(image_path):
    image = get_file_content(image_path)
    # 调用通用文字识别, 图片参数为本地图片
    result = client.basicAccurate(image, False)
    #result的type为字典，形如
    #{'log_id': ***, 'words_result_num': 1, 'words_result': [{'words': '行动结束'}]}
    #print('type of result is', type(result))
    #print(result)
    # 结果拼接返回
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])

# if __name__ == '__main__':
#     print(img_to_str('screen/end/end.png'))

