from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#合并ini与抠图图片
def blend_two_images():
    img1 = Image.open("103_ini.png ")
    img1 = img1.convert('RGBA')

    img2 = Image.open("result2.png ")
    img2 = img2.convert('RGBA')

    img = Image.blend(img1, img2, 0.5)
    print(type(img))
    img.save("result.png")
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return
blend_two_images()
