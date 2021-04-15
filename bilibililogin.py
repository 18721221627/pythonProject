#login_bilibili
from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains #导入动作链模块
from interface import base64_api
#快打码平台！
KUAI_USERNAME = '18721221627'
KUAI_PASSWORD = 'JABIL12345'

USERNAME = '18721221627'
PASSWORD = 'JABIL12345'

#创建浏览器对象
driver = webdriver.Chrome(r'D:\chromedriver.exe')
#打开请求网页页面
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10) #隐式等待浏览器渲染完成，sleep是强制等待
#driver.execute_script("document.body.style.zoom='0.67'") #浏览器内容缩放67%
driver.maximize_window()#最大化浏览器

'''
用selenium自动化工具操作浏览器，操作的顺序和平常用浏览器操作的顺序是一样的
'''

'''
找到用户名和密码框输入密码
'''
user_input = driver.find_element_by_xpath('//*[@id="login-username"]') #使用xpath定位用户名标签元素
user_input.send_keys(USERNAME)
time.sleep(1)

user_input = driver.find_element_by_xpath('//*[@id="login-passwd"]') #用户密码标签
user_input.send_keys(PASSWORD)
time.sleep(1)

#点击登录
Login_input = driver.find_element_by_css_selector('#geetest-wrap > div > div.btn-box > a.btn.btn-login')
Login_input.click()
time.sleep(5)
#对图片验证码进行提取----关键点！！！！这里能否提取正确直接关系到第三方是否能够正确识别！
img_label =driver.find_element_by_xpath('/html/body/div[3]/div[2]')

#img_label = driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div') #提取图片标签
#保存图片
driver.save_screenshot('login.png') #截取当前整个页面
time.sleep(5)
#location可以获取这个元素左上角坐标
#print(img_label.location)
#size可以获取这个元素的宽(width)和高(height)
print(img_label.size)

#计算验证码的左右上下横切面
left = img_label.location['x']
top = img_label.location['y']
right = img_label.location['x'] + img_label.size['width']
down = img_label.location['y'] + img_label.size['height']

im = Image.open('login.png')
im = im.crop((left,top,right,down))
im.save('yzm.png')

#对接打码平台


img_path = 'yzm.png'
result = base64_api(uname=KUAI_USERNAME, pwd=KUAI_PASSWORD, img=img_path,tid=27)#tid 为验证码识别类型，注意看官网介绍！
#登录页面的坐标
#print(result)
print('验证码识别结果：', result)
result_list = result.split('|')
for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]
    ActionChains(driver).move_to_element_with_offset(img_label, int(x), int(y)).click().perform()  # perform()执行整个动作链

#点击确认按钮
driver.find_element_by_css_selector('body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div > div.geetest_panel > a > div').click()
input()  # 用户输入 阻塞浏览器关闭
# 关闭浏览器
driver.quit()
