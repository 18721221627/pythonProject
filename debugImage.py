
from PIL import Image

image = Image.open('login.png')
weight, height = image.size
# 这里的比例需要自己摸索，实际上只需要横坐标准确即可--这里是关键反复调试
box = (weight * 1/2 - 270, height * 1/2 - 280, weight * 1/2 + 280, height * 1/3 + 375)
region = image.crop(box)
region.save('yzm.png')