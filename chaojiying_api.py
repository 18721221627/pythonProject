import requests

import json
#接口调用超级鹰
im = open('yzm.png', 'rb').read()
files = {'userfile':im}

params = {
    'user': '18721221627',  #你的平台用户名
    'pass':'JABIL12345',   #你的平台密码
    'softid': '910775',  #你的6位平台ID，见用户中心-软件ID
    'codetype':'9004'    #验证码类别代码，此处代表1-6位字母数字，详情见平台价格体系
        }

headers = {
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
}

r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=headers)
#返回json
r1=(r.json())
#获取json的pic_str----pic_str为具体识别信息！
distance = r1['pic_str']
print(distance)

