
from PIL import Image

image = Image.open('login.png')
weight, height = image.size
# 这里的比例需要自己摸索，--这里是关键反复调试
box = (weight * 1/2 - 50, height * 1/2 +30, weight * 1/2 + 350, height * 1/2 + 275)
region = image.crop(box)
region.save('yzm.png')