#快识别网址 http://www.kuaishibie.cn/
#interface
import base64
import json
import requests

def base64_api(uname,pwd,img,tid):
    '''
    验证码识别接口
    :param uname: 快识别用户名
    :param pwd: 快识别密码
    :param img: 图片路径
    :return: 返回识别结果
    '''
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64,"typeid": tid}
    #result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    result = json.loads(requests.post("http://api.ttshitu.com/imageXYPlus", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
