# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=li5ObCpnNGNGZq7BL6H6298V&client_secret=LqzImHEIS6UGZIH5uu8M0Et9UsmFckah'
response = requests.get(host)
if response:
    print(response.json())
