

#chpp  //*[@id="root"]/div/div[2]/div/div[2]/form/div[3]/div/div/span/div/img

import time
from selenium import webdriver
from PIL import Image
from Test import Chaojiying_Client
from selenium.webdriver.chrome.options import Options

# 创建一个浏览器
browser = webdriver.Safari()
chrome_options = Options()

# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#chrome_options.add_experimental_option('--disable-gpu')
time.sleep(1)
# 访问登录页面
url = 'http://wlhyp.utrailertj.com/login.html'
time.sleep(3)
# 设置界面最大化
browser.maximize_window()
browser.get(url)


#将当前页面截图保存在当前项目
time.sleep(3)

browser.save_screenshot('login.png')
#验证码元素
yzm_btn = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[3]/div/img')

image = Image.open('login.png')
weight, height = image.size
    # 这里是重点要反复的调--------------------------------------调试将整个验证码区域传给第三方打码平台
        # weight第一个调试左边 height第一个提示上边  weight第二个调试右边  height第二个调试下边
box = (weight * 1 / 2 +735, height * 1 / 2 , weight * 1 / 2 +998, height * 1 / 3+335 )
region = image.crop(box)
region.save('yzm.png')

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
browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/input').send_keys('18515491990')
#输入密码

browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/input').send_keys('123qweAA')
# 在输入框输入验证码
yzm_input = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[3]/input')
yzm_input.send_keys(distance)
time.sleep(3)
#点击登录
browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div[2]').click()

time.sleep(10)

browser.quit()