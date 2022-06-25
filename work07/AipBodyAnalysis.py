from aip import AipBodyAnalysis
from concurrent.futures import ThreadPoolExecutor
import MyImage


# https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
class BodyAnalysis:
    def __init__(self):
        self.client = AipBodyAnalysis("", "", "")
        # 定义多线程池
        self.pool = ThreadPoolExecutor(2)

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipBodyAnalysis(appid, apikey, secretkey)
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

    def gesture(self, file):
        """ 调用手势识别 """
        resp = self.client.gesture(self.getFileContent(file))
        data = ""
        for res in resp["result"]:
            data += f"类型：{res['classname']}，置信度：{res['probability']}\n"
        return data

    def bodyNum(self, file):
        """ 调用人流量统计 """
        """ 如果有可选参数 """
        options = {}
        options["show"] = "true"
        resp = self.client.bodyNum(self.getFileContent(file), options)
        return resp["person_num"], resp["image"]

    def bodyAnalysis(self, file):
        """ 调用人体关键点识别 """
        resp = self.client.bodyAnalysis(self.getFileContent(file))
        body_parts = resp["person_info"][0]["body_parts"]
        return body_parts
