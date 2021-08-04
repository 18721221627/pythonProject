from PIL import Image

image = Image.open('login.png')
weight, height = image.size
    # 这里是重点要反复的调--------------------------------------调试将整个验证码区域传给第三方打码平台
        # weight第一个调试左边 height第一个提示上边  weight第二个调试右边  height第二个调试下边
box = (weight * 1 / 2 +735, height * 1 / 2 , weight * 1 / 2 +998, height * 1 / 3+335 )

print(box,'打印')
region = image.crop(box)
region.save('yzm.png')

