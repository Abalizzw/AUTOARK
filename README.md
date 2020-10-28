# AUTOARK
Auto daily activity program of Ark-Nights with OpenCV, MuMu simulator adb and Baidu API.

## Configuration

1. OpenCV
```
pip install opencv-python
```
2. Baidu API
```
pip install baidu-aip
```
3.

## Setup in Windows10
Dowload this code and unzip into your path.
Open cmd and enter the local path by commanding:
```
>/your local path/[for example my path is D:\AUTOARK-master]
```


#### Install baidu API

Sign up an account of [Baidu API](https://login.bce.baidu.com/), it is free.
Check the [document](https://cloud.baidu.com/doc/OCR/index.html) to install related packages. (I will write it in detail later.)
After successful applying the OCR and image recogition API, copy 3 keys and paste them to these lines in 2 files (\AUTOARK-master\baidulib\ocr.py & \AUTOARK-master\baidulib\img_search.py).
```
config = {
    'appId': '********',
    'apiKey': '************************',
    'secretKey': '********************************'
}
```

#### Get start
1. Open MuMu simulator.
2. Run the `adb_init_connect.py` in cmd
```
python adb_init_connect.py
```
  In this file line6 _127.0.0.1:7555_ is the id for [MuMu](https://mumu.163.com/) simulator, please convert it to your simulator's id before running this file.

3. Make sure to enter the main interface of the game.

4. Run the spcific function file by python command. For example, buy the credit store's goods by command:
```
python shop.py
```

#### Preview
![image](image/MuMu20201028150640.png)

and more..

