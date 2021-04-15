import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        # 更改点一
        self.password = md5(password.encode("utf-8")).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

    def run(self):
     chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
     im = open('yzm.png', 'rb').read()
     result = chaojiying.PostPic(im,3004)
     return result['pic_str']
if __name__ == '__main__':
    # 更改点二，输入注册的账号与密码，软件ID
    chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
    # 更改点三：使用本地图片文件路径 来替换 a.jpg,有时WIN系统须要//
    im = open('yzm.png', 'rb').read()
    # 更改点四：1902表示验证码类型，使用者可以根据自己的验证码类型进行修改，在官网测试案例可以查看
    print(chaojiying.PostPic(im, 1902))