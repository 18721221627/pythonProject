from PIL import Image

image = Image.open('login.png')
weight, height = image.size
    # 这里是重点要反复的调--------------------------------------调试将整个验证码区域传给第三方打码平台
        # weight第一个调试左边 height第一个提示上边  weight第二个调试右边  height第二个调试下边
box = (weight * 1 / 2 - 25, height * 1 / 2 - 50, weight * 1 / 2 + 428, height * 1 / 2+235 )

print(box,'打印')
region = image.crop(box)
region.save('yzm.png')

