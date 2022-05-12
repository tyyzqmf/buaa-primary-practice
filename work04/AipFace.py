from aip import AipFace
import base64
import const


# https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
class Face:
    def __init__(self):
        self.client = AipFace("", "", "")

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipFace(appid, apikey, secretkey)
        # 校验密钥是否正确
        try:
            authObj = self.client._auth()
            params = self.client._getParams(authObj)
            return True
        except Exception as e:
            return False

    def detect(self, file):
        """ 调用人脸检测 """
        imageType = "BASE64"
        options = {}
        options["face_field"] = "age,beauty,expression,face_shape,gender,glasses"
        image = bytes.decode(base64.b64encode(open(file, 'rb').read()))
        resp = self.client.detect(image, imageType, options)
        data = ''
        if resp["error_code"] == 0:
            faceData = resp["result"]['face_list'][0]
            data += f"估算年龄: {int(faceData['age'])} \n"
            data += f"美丑打分: {int(faceData['beauty'])} \n"
            data += f"表情: {const.EXPRESSION[faceData['expression']['type']]}，置信度: {faceData['expression']['probability']} \n"
            data += f"脸型: {const.FACESHAPE[faceData['face_shape']['type']]}，置信度: {faceData['face_shape']['probability']} \n"
            data += f"性别: {const.GENDER[faceData['gender']['type']]}，置信度: {faceData['gender']['probability']} \n"
            data += f"是否带眼镜: {const.GLASSES[faceData['glasses']['type']]}，置信度: {faceData['glasses']['probability']} \n"
        else:
            data = resp["error_msg"]
        return data

    def match(self, file1, file2):
        resp = self.client.match([
            {
                'image': bytes.decode(base64.b64encode(open(file1, 'rb').read())),
                'image_type': 'BASE64',
            },
            {
                'image': bytes.decode(base64.b64encode(open(file2, 'rb').read())),
                'image_type': 'BASE64',
            }
        ])
        data = ''
        if resp["error_code"] == 0:
            data += f"人脸相似度得分: \n{resp['result']['score']} \n"
        else:
            data = resp["error_msg"]
        return data
