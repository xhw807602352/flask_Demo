#! usr/bin/python3
# -*-coding: utf-8-*-
# Author: frankle
# Date: 2019/6/5 20:49
# FileName: CarDetect.py
# Software: PyCharm
from aip import AipImageClassify
import requests as rq


# import pymysql as db
# mydb = db.connect("localhost", "root", "123456", 'mydb')
# cursor = mydb.cursor()
# data = cursor.execute("select * from mytb")
# one = cursor.fetchall()
# print(one, data)
""" 你的 APPID AK SK """
APP_ID = '16440799'
API_KEY = 'cFcPI11uqzTxtFHPoKZRdO6X'
SECRET_KEY = 'c56TSZRVnSV9LfdMwD16P0xH7Ovo8YRW'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
client.setConnectionTimeoutInMillis(1000*10)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def url_imgage(url):
    req = rq.get(url)
    return req.content

def get_id(car):
    car_ret = []
    for j in car["result"]:
        for k in j["List"]:
            for o in k["List"]:
                # t = {o["N"]: o["I"]}
                car_ret.append(o)
    return car_ret

if __name__ == "__main__":
    image = get_file_content('static/1.jpg')
    url= "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559819550562&di=2144b5c059daf2096558c9e05bf7da7e&imgtype=0&src=http%3A%2F%2Fpic.baike.soso.com%2Fp%2F20120114%2F20120114151019-1830199455.jpg"
    image = url_imgage(url)

    """ 调用车辆识别 """
    client.carDetect(image)

    """ 如果有可选参数 """
    options = {}
    options["top_num"] = 1
    # options["baike_num"] = 5

    """ 带参数调用车辆识别 """
    out = client.carDetect(image, options)
    # print(out)
    # 车名
    # print(out["result"][0]["name"])
    # 搜索车名id和车系id

    # 车辆详细
    # brand_api = "http://apis.haoservice.com/lifeservice/car/GetSeries"
    # serial_api = "http://apis.haoservice.com/lifeservice/car/GetModel/"
    # type_api = "http://apis.haoservice.com/lifeservice/car"
    # id = 117
    # para = {"key": "d22ad5453ce14ae18dc9c07c220321a5", "id": id}
    # req = rq.get(serial_api, params=para)
    # print(req.text)
    # type_id = \
    #     {'error_code': 0, 'reason': 'Success', 'result': {' I': 266, 'List': [{'I': 2, 'N': '停售车型', 'List': [{'I': 2016, 'List': [{'I': 24530, 'N': '6.0L GT邦德限量版', 'P': 3888000}]}, {'I': 2015, 'List': [{'I': 25149, 'N': '6.0L Coupe', 'P': 3418000}, {'I': 25150, 'N': '6.0L Volante', 'P': 3738000}]}, {'I': 2014, 'List': [{'I': 18449, 'N': '6.0L Carbon Black Coupe', 'P': 3588800}, {'I': 19652, 'N': '6.0L Carbon White Coupe', 'P': 3588800}, {'I': 17377, 'N': '6.0L Coupe百年纪念版', 'P': 4180000}, {'I': 17378, 'N': '6.0L Volante百年纪念版', 'P': 4380000}]}, {'I': 2013, 'List': [{'I': 13904, 'N': '6.0L Coupe', 'P': 3388800}]}, {'I': 2011, 'List': [{'I': 8048, 'N': '6.0L Touchtronic Coupe', 'P': 3390000}, {'I': 8049, 'N': '6.0L Touchtronic Volante', 'P': 3450000}]}, {'I': 2007, 'List': [{'I': 3491, 'N': '6.0L Manual Coupe', 'P': 3199000}, {'I': 5527, 'N': '6.0L Touchtronic Coupe', 'P': 3259000}, {'I': 3492, 'N': '6.0L Manual Volante', 'P': 3399000}, {'I': 3536, 'N': '6.0L Touchtronic Volante', 'P': 3499000}]}, {'I': 2004, 'List': [{'I': 1369, 'N': '6.0L', 'P': 1430000}, {'I': 1408, 'N': '6.0L Coupe', 'P': 1540000}]}]}]}}