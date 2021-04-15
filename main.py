import time
from selenium import webdriver
from PIL import Image
from Test import Chaojiying_Client
from selenium.webdriver.chrome.options import Options

# 创建一个浏览器
browser = webdriver.Chrome(r'D:\chromedriver.exe')
chrome_options = Options()

# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#chrome_options.add_experimental_option('--disable-gpu')
time.sleep(1)
# 访问登录页面
url = 'http://www.chaojiying.com/user/mysoft/'
time.sleep(3)
# 设置界面最大化
browser.maximize_window()
browser.get(url)

# 选择账号、密码输入栏，输入对应的账号密码
input_user = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input')
input_user.send_keys('18721221627')
input_pwd = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')
input_pwd.send_keys('JABIL12345')

#将当前页面截图保存在当前项目
browser.save_screenshot('login.png')
# 这个是验证码图片的元素
yzm_btn = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img')

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
# 通过上下左右的  值，去截取验证码
yzm_pic = login_pic.crop(val)
yzm_pic.save('yzm.png')

# 识别验证码并保存
cjy = Chaojiying_Client('1872121627', 'JIL12345', '910775').run()  # 调用超级鹰的run方法 进行第三方识别


print('验证码是',cjy)

# 在输入框输入验证码
yzm_input = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')
yzm_input.send_keys(cjy)


# 点击登录
submit = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input')
time.sleep(5)
submit.click()
time.sleep(10)

browser.quit()