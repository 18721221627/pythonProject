from selenium import webdriver
from selenium.webdriver import ActionChains
from chaojiying import Chaojiying_Client
from PIL import Image
#12306 已经识别！
import time

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
# 防止12306禁止selenium
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
driver.execute_script(script)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('18721221627')
driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('123456')

# 直接定位验证码图片标签位置截图
#img = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
#img.driver.save_screenshot('login.png')
# 获取验证码图片坐标
driver.save_screenshot('login.png')
img = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
location = img.location  # 左上角坐标 x,y
size = img.size  # 长 宽
rangle = (int(location['x']), int(location['y']),
           int(location['x'])+size['width'], int(location['y'])+size['height'])

# 根据坐标截取 验证码图片
img_code = Image.open('login.png')
frame = img_code.crop(rangle)
frame.save('yzm.png')

# 超级鹰识别验证码 返回坐标值
chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
im = open('yzm.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']
print('识别结果',result)

# 动作链点击坐标
all_list = []
if '|' in result:
    list_item = result.split('|')
    count = len(list_item)
    for i in range(count):
        x_y = []
        x = int(list_item[i].split(',')[0])
        y = int(list_item[i].split(',')[1])
        x_y.append(x)
        x_y.append(y)
        all_list.append(x_y)
else:
    x_y = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    x_y.append(x)
    x_y.append(y)
    all_list.append(x_y)
print(all_list)

for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(driver).move_to_element_with_offset(
        img, x, y).click().perform()
    time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(3)

span = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
action = ActionChains(driver)
action.click_and_hold(span)
action.move_by_offset(350, 0).perform()
action.release()

time.sleep(5)

driver.quit()
