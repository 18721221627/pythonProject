from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import cv2
import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
#虎嗅---已成功！
from chaojiying import Chaojiying_Client
import requests
from hashlib import md5


class main():
    def __init__(self):
        self.url = 'https://www.huxiu.com/'
        #self.file_path = 'D://Program Files//1.png'
        #self.file_path2 = 'D://Program Files//2.png'
        self.distance = 0
        self.key = 0

    # 启动浏览器
    def Launch_browser(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="header-nav"]/nav/ul/li[7]/div/img').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/p/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[1]/div/div[1]/div[2]/input').send_keys('18721221627')
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[1]/div/div[2]/button/span').click()
        time.sleep(4)


    # 截图
    def get_picture(self):
        self.driver.find_element_by_xpath('//*[@id="geetest-box-login"]/div[2]/div[3]/div[2]').click()
        self.driver.save_screenshot('login.png')

    # 分割截图获取验证码图片
    def crop_picture(self):
        image = Image.open('login.png')
        weight, height = image.size
        # 这里是重点要反复的调--------------------------------------调试将整个验证码区域传给第三方打码平台
        # weight第一个调试左边 height第一个提示上边  weight第二个调试右边  height第二个调试下边
        box = (weight * 1 / 2 - 139, height * 1 / 2 - 120, weight * 1 / 2 + 128, height * 1 / 2-15 )


        print(box,'打印')
        region = image.crop(box)
        region.save('yzm.png')
        #进行灰度处理！
        #cv2.imwrite('yzm.png', cv2.cvtColor(cv2.imread('yzm.png'), cv2.COLOR_RGB2GRAY))

        # 超级鹰
    def cjy(self):
        # 用户中心>>软件ID 生成一个替换 910001
        self.chaojiying = Chaojiying_Client('18721221627', 'JABIL12345', '910775')
        # chaojiying = Chaojiying_Client('超级鹰用户名', '超级鹰密码', '910001')
        # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        im = open('yzm.png', 'rb').read()
        # 9101 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        # 咨询了一下滑动验证码是选择9101
        re = self.chaojiying.PostPic(im, 9101)
        print('我是返回数据',re)
        # print(re['pic_str'])

        # 减去一半滑块长度---这个长度要反复的调试！
        self.distance = int(re['pic_str'].split(',')[0])-32

        print(self.distance,'长度')


        self.im_id = re['pic_id']
        print(self.im_id)

    # 获取轨迹
    def get_track(self):
        # 轨迹
        self.track = []
        # 设置一个分隔线，之前为匀加速运动，之后为匀减速运动
        mid = self.distance * 4 / 5
        # 用于记录当前的移动距离
        current = 0
        # 时间间隔
        t = 0.2
        # 初速度
        v = 0

        while current < self.distance:
            if current < mid:
                a = 8
            else:
                a = -12
            v0 = v
            v = v0 + a * t
            move = v * t + 1 / 2 * a * t * t
            current += move
            self.track.append(round(move))
        print(self.track)

    # 模拟移动https://www.processon.com/diagraming/60535f626376894e1e941bf1
    def move(self):
        # 直接移动到指定坐标
        self.track = [self.distance]

        # 点击和按住
        element1=self.driver.find_element_by_xpath('//*[@id="geetest-box-login"]/div[2]/div[3]/div[2]')
        ActionChains(self.driver).click_and_hold(element1).perform()
        # 拖动
        for x in self.track:
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(3)
        # 松开鼠标
        ActionChains(self.driver).release().perform()

    # 检测结果(目前不做检测，先白嫖一下)
    def check(self):
        if self.key ==1:
            pass
        # 出错时反馈给超级鹰，取消扣分
        else:
            re = self.chaojiying.ReportError(self.im_id)
            print('识别出错了',re)

    # 关闭浏览器
    def quit(self):
        time.sleep(5)
        self.driver.quit()



    # main方法
    def main(self):
        self.Launch_browser()
        self.get_picture()
        self.crop_picture()

        self.cjy()
        # 目前选择直接跳到缺口
        self.get_track()
        self.move()
        self.check()
        self.quit()


if __name__ == '__main__':
    ma = main()
    ma.main()










