from PIL import Image
import re
import base64
from io import BytesIO


class MyImage:
    """图片处理类"""

    def __init__(self, filename, canvas_size=(200, 200)):
        # 原始图片
        self.filename = filename
        self.photo = Image.open(self.filename).convert('RGB')
        # 原始图片大小
        self.size = self.photo.size
        # 画布大小
        self.canvas_size = canvas_size
        # 处理后图片路径
        self.dealname = './tmp.gif'
        # 处理后图片大小
        self.dealsize = canvas_size
        # 缩放比
        self.scale = 1.0

    # 处理图片
    def deal(self):
        # 等比例放缩
        # 画布长宽比例
        canvasXY = self.canvas_size[0] / self.canvas_size[1]
        # 原始图片长宽比例
        sizeXY = self.size[0] / self.size[1]

        if canvasXY >= sizeXY:
            # 按Y轴比例缩放
            self.scale = self.canvas_size[1] / self.size[1]
        else:
            # 按X轴比例缩放
            self.scale = self.canvas_size[0] / self.size[0]

        self.dealsize = (int(self.size[0] * self.scale), int(self.size[1] * self.scale))

        photo = Image.open(self.filename).convert('RGB')
        photo = photo.resize(self.dealsize)  # 图片大小转换
        # save会根据后缀名转换为特定格式
        photo.save(self.dealname)

    # base64转换
    def base64ToImage(self, base64_str):
        base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        img.save(self.dealname)
