

#chpp  //*[@id="root"]/div/div[2]/div/div[2]/form/div[3]/div/div/span/div/img

import time
import os
import pytest
import allure
from chaojiying import Chaojiying_Client
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.options import Options

# 创建一个浏览器
def test_steps_demo():

    browser = webdriver.Safari()
    chrome_options = Options()

# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#chrome_options.add_experimental_option('--disable-gpu')
    time.sleep(1)
    # 访问登录页面
    url = 'https://test-appapis-1.95155.com/lhjh-support-web/website.jsp'
    time.sleep(2)
    # 设置界面最大化
    browser.maximize_window()
    browser.get(url)


    #将当前页面截图保存在当前项目
    time.sleep(3)

    browser.save_screenshot('login.png')
    #验证码元素
    yzm_btn = browser.find_element_by_id('imgCode_img')
    #打开截图
    image = Image.open('login.png')
    weight, height = image.size
    box = (weight * 1/2 - 50, height * 1/2 +30, weight * 1/2 + 350, height * 1/2 + 275)
    print(box,'打印')
    region = image.crop(box)
    region.save('yzm.png')
    #调用超级鹰的方法！
    chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
    #chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰密码', '换成自己的id')
    #打开验证码并且读取数据保存！
    im = open('yzm.png', 'rb').read()
    #将要识别的验证码类型传过去---具体验证码类型参考第三方打码平台代码！
    re = chaojiying.PostPic(im, 4004)
    print('我是返回数据', re)
    #返回的数据是个json我们要获取pic_str，这个就是验证码识别的结果！
    distance = re['pic_str']


    print('验证码是',distance)
    #输入账号
    browser.find_element_by_id('userName').send_keys('admin')
    #输入密码

    browser.find_element_by_id('password').send_keys('321')
    # 在输入框输入验证码
    yzm_input = browser.find_element_by_id('imgCode')
    yzm_input.send_keys(distance)
    time.sleep(3)
    #点击登录
    browser.find_element_by_id('loginSubmit').click()

    time.sleep(10)
    #退出浏览器
    browser.quit()
assert True
if __name__ == '__main__':
    pytest.main(['--alluredir', './reports/result'])
    os.system('allure generate ./reports/result -o ./reports/report --clean')
#browser.quit()
