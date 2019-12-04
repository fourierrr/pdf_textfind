# 导入相关的库
from PIL import Image
# 打开一张图

def save_pic(imgpath):

    img = Image.open(imgpath)
    # 图片尺寸
    img_size = img.size
    height = img_size[1]  # 图片高度
    width = img_size[0]  # 图片宽度

    for (k,v) in {"a":0.05,"b":0.35,"c":0.65}.items():
        # x = 0.05 * width
        # x = 0.35 * width
        # x = 0.65 * width

        x= v * width
        y = 0.07 * height
        w = 0.3 * width
        h = 0.83 * height

        # 开始截取
        region = img.crop((x, y, x + w, y + h))
        # 保存图片
        region.save(imgpath.replace(".jpg","")+k+".jpg")
        print(k+"  finish...")

path='贵州年鉴2012_2.jpg'
save_pic(path)