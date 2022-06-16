from PIL import Image


class MyImage:
    """图片处理类"""

    def __init__(self, filename):
        # 原始图片
        self.filename = filename
        self.photo = Image.open(self.filename).convert('RGB')
        # 原始图片大小
        self.size = self.photo.size
        # 处理后图片路径
        self.dealname = './tmp.gif'
        # 处理后图片大小
        self.dealsize = (250, 250)

    # 处理图片
    def deal(self):
        photo = Image.open(self.filename).convert('RGB')
        photo = photo.resize(self.dealsize)  # 图片大小转换
        # save会根据后缀名转换为特定格式
        photo.save(self.dealname)

    # 在处理后的图片上画框，坐标转换
    def rectangle(self, top, left, width, height):
        x = 250 / self.size[0]
        y = 250 / self.size[1]
        x1 = left * x
        y1 = (top + height) * y
        x2 = (left + width) * x
        y2 = top * y
        return (x1, y1), (x2, y2)
