# encoding:utf-8

import requests
import base64

'''
OCR 通用识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
# 二进制方式打开图片文件
f = open('2-1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.6e9a734aaaa6fda770180ac481675d66.2592000.1578020955.282335-10688440'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
