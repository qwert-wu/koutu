from PIL import Image
import numpy as np
import PIL.ImageOps
import matplotlib.pyplot as plt
import scipy.misc
img1 = Image.open('103_gt.png')
im1 = np.array(img1)
img2 = Image.open('103_pred.png')
im2 = np.array(img2)
#将gt与pred相同像素值部分转为黑色生成图片o1
for i in range(511):
    for j in range(511):
        a = im1[i, j]
        b = im2[i, j]
        if a == b:
            im1[i, j] = 255
            im2[i, j] = 255
#创建全零矩阵
zeros1 = np.zeros((512, 512))
scipy.misc.imsave('o1.png', im1)
image = Image.open('o1.png')
#o1图片黑白对调
fan = PIL.ImageOps.invert(image)
fan.save('fan.png')
he2 = np.array(fan)
#gt与pred图片相同部分为红色，不同为黑色
rgb = np.dstack((fan, zeros1, zeros1))
scipy.misc.imsave('jie.png', rgb)
#读取gt图片，白色区域填充为绿色
im0 = np.array(img1)
rgb1 = np.dstack((zeros1, im0, zeros1))
scipy.misc.imsave('guo.png', rgb1)
#将gt与pred抠图合并
img1 = Image.open("guo.png ")
img1 = img1.convert('RGBA')

img2 = Image.open("jie.png ")
img2 = img2.convert('RGBA')

img = Image.blend(img1, img2, 0.5)
print(type(img))
img.save("result2.png")
plt.imshow(img)
plt.axis('off')
plt.show()
