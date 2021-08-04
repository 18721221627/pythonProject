

#chpp  //*[@id="root"]/div/div[2]/div/div[2]/form/div[3]/div/div/span/div/img

import time
from selenium import webdriver
from PIL import Image
from Test import Chaojiying_Client
from selenium.webdriver.chrome.options import Options

# 创建一个浏览器
browser = webdriver.Chrome()
chrome_options = Options()

# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#chrome_options.add_experimental_option('--disable-gpu')
time.sleep(1)
# 访问登录页面
url = 'https://www.gghypt.net/'
time.sleep(3)
# 设置界面最大化
browser.maximize_window()
browser.get(url)

#将当前页面截图保存在当前项目
time.sleep(3)

browser.save_screenshot('login.png')
#验证码元素
yzm_btn = browser.find_element_by_id('imgCode_img')

# 获取图片元素的位置
loc = yzm_btn.location
# 获取图片的宽高-----如果自己的电脑分辨率不是百分百 那么要调整！
size = yzm_btn.size
left = loc['x'] # 计算左边界
top = loc['y']  # 计算上边界
right = (loc['x'] + size['width'])    # 计算右边界
botom = (loc['y'] + size['height'])   # 计算下边界
# 将上下左右边界值放到元祖中（注意顺序：左 上 右  下）
local = (left, top, right, botom)


botom = yzm_btn.location['y']+yzm_btn.size['height']
val = (left, top, right, botom)
print(left,top,right,botom)
# 打开网页截图
login_pic = Image.open('login.png')
# 通过上下左右的值，去截取验证码
yzm_pic = login_pic.crop(val)
yzm_pic.save('yzm.png')


#调用超级鹰的方法！
chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
#chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰密码', '换成自己的id')
#打开验证码并且读取数据保存！
im = open('yzm.png', 'rb').read()
#将要识别的验证码类型传过去---具体验证码类型参考第三方打码平台代码！
re = chaojiying.PostPic(im, 3004)
print('我是返回数据', re)
#返回的数据是个json我们要获取pic_str，这个就是验证码识别的结果！
distance = re['pic_str']


print('验证码是',distance)
#输入账号
browser.find_element_by_id('userName').send_keys('zhanghg01')
#输入密码

browser.find_element_by_id('password').send_keys('zhanghegao138')
# 在输入框输入验证码
yzm_input = browser.find_element_by_id('imgCode')
yzm_input.send_keys(distance)
time.sleep(3)
#点击登录
browser.find_element_by_id('loginSubmit').click()

time.sleep(10)

browser.quit()