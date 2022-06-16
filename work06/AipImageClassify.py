from aip import AipImageClassify
from concurrent.futures import ThreadPoolExecutor
import MyImage


# https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
class ImageClassify:
    def __init__(self):
        self.client = AipImageClassify("", "", "")
        # 定义多线程池
        self.pool = ThreadPoolExecutor(2)

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipImageClassify(appid, apikey, secretkey)
        # 校验密钥是否正确
        try:
            authObj = self.client._auth()
            params = self.client._getParams(authObj)
            return True
        except Exception as e:
            return False

    def getFileContent(self, filepath):
        """ 读取文件 """
        with open(filepath, "rb") as fp:
            return fp.read()

    def threadPoolClassify(self, file, with_face=0):
        """ 多线程识别 """
        # 任务1：通用物体及场景识别
        job1 = self.pool.submit(self.advancedGeneral, file)
        # 任务2：图像单主体检测
        job2 = self.pool.submit(self.objectDetect, file, with_face)

        # 返回结果
        data = "【通用物体和场景识别】\n"
        data += f"{job1.result()}\n"
        data += "【图像主体检测】\n"
        data += f"{job2.result()}"

        image = MyImage.MyImage(file)
        p1, p2 = image.rectangle(
            job2.result()['top'],
            job2.result()['left'],
            job2.result()['width'],
            job2.result()['height']
        )

        return data, p1, p2

    def advancedGeneral(self, file):
        """ 调用通用物体和场景识别 """
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = 1
        resp = self.client.advancedGeneral(self.getFileContent(file), options)
        return resp["result"][0]["baike_info"]["description"]

    def objectDetect(self, file, with_face=0):
        """ 调用图像主体检测 """
        """ 如果有可选参数 """
        options = {}
        options["with_face"] = with_face
        resp = self.client.objectDetect(self.getFileContent(file), options)
        return resp["result"]

    def dishDetect(self, file):
        """ 菜品识别 """
        resp = self.client.dishDetect(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['name']}，置信度：{res['probability']}\n"
        return data

    def carDetect(self, file):
        """ 车辆识别 """
        resp = self.client.carDetect(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['name']}，置信度：{res['score']}\n"
        return data

    def logoSearch(self, file):
        """ 商标识别 """
        resp = self.client.logoSearch(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['name']}，置信度：{res['probability']}\n"
        return data

    def animalDetect(self, file):
        """ 动物识别 """
        resp = self.client.animalDetect(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['name']}，置信度：{res['score']}\n"
        return data

    def plantDetect(self, file):
        """ 植物识别 """
        resp = self.client.plantDetect(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['name']}，置信度：{res['score']}\n"
        return data
