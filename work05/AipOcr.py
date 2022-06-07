from aip import AipOcr
import base64
import const


# https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
class Ocr:
    def __init__(self):
        self.client = AipOcr("", "", "")

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipOcr(appid, apikey, secretkey)
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

    def allGeneral(self, file, precision="base", detect_direction="false", vertexes_location="false"):
        """ 通用文字识别 """
        if file == "":
            return ""
        # 如果有可选参数
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = detect_direction
        options["vertexes_location"] = vertexes_location
        # 判断调用接口
        if precision == "base" and vertexes_location == "false":
            # 通用文字识别（标准版）
            resp = self.client.basicGeneral(self.getFileContent(file), options)
        elif precision == "base" and vertexes_location == "true":
            # 通用文字识别（标准含位置版）
            resp = self.client.general(self.getFileContent(file), options)
        elif precision == "high" and vertexes_location == "false":
            # 通用文字识别（高精度版）
            resp = self.client.basicAccurate(self.getFileContent(file), options)
        elif precision == "high" and vertexes_location == "true":
            # 通用文字识别（高精度含位置版）
            resp = self.client.accurate(self.getFileContent(file), options)
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            # 识别方向
            if detect_direction == "true":
                data += f"【识别方向】：{const.DIRECTION[resp['direction']]} \n"
            # 识别文字
            words_result = resp["words_result"]
            data += f"【识别文字】："
            for word in words_result:
                # 位置信息
                if vertexes_location == "true":
                    data += f"{word['words']}" \
                            f"（位置：" \
                            f"{word['location']['left']}," \
                            f"{word['location']['top']}," \
                            f"{word['location']['width']}," \
                            f"{word['location']['height']}" \
                            f"），"
                else:
                    data += f"{word['words']}，"
            data = data[:-1]
        return data

    def webImage(self, file, detect_direction="false"):
        """ 网络图片文字识别 """
        if file == "":
            return ""
        # 如果有可选参数
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = detect_direction
        resp = self.client.webImage(self.getFileContent(file), options)
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            # 识别方向
            if detect_direction == "true":
                data += f"【识别方向】：{const.DIRECTION[resp['direction']]} \n"
            # 识别文字
            words_result = resp["words_result"]
            data += f"【识别文字】："
            for word in words_result:
                data += f"{word['words']}，"
            data = data[:-1]
        return data

    def idCard(self, file, id_card_side="front"):
        """ 身份证识别 """
        if file == "":
            return ""
        resp = self.client.idcard(self.getFileContent(file), id_card_side=id_card_side)
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            if resp["image_status"] != "normal":
                return const.IMAGESTATUS[resp["image_status"]]
            words_result = resp["words_result"]
            for key, value in words_result.items():
                data += f"{key}: {value['words']}，"
        return data

    def bankCard(self, file):
        """ 银行卡识别 """
        if file == "":
            return ""
        resp = self.client.bankcard(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            data += f"银行卡号: {resp['result']['bank_card_number']}\n"
            data += f"银行: {resp['result']['bank_name']}\n"
            data += f"银行卡类型: {const.BANKCARDTYPE[resp['result']['bank_card_type']]}\n"
        return data

    def drivingLicense(self, file):
        """ 驾驶证识别 """
        if file == "":
            return ""
        resp = self.client.drivingLicense(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            words_result = resp["words_result"]
            for key, value in words_result.items():
                data += f"{key}: {value['words']}，"
        return data

    def vehicleLicense(self, file):
        """ 行驶证识别 """
        if file == "":
            return ""
        resp = self.client.vehicleLicense(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            words_result = resp["words_result"]
            for key, value in words_result.items():
                data += f"{key}: {value['words']}，"
        return data

    def businessLicense(self, file):
        """ 营业执照识别 """
        if file == "":
            return ""
        resp = self.client.businessLicense(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            words_result = resp["words_result"]
            for key, value in words_result.items():
                data += f"{key}: {value['words']}，"
        return data

    def licensePlate(self, file):
        """ 车牌识别 """
        if file == "":
            return ""
        resp = self.client.licensePlate(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            words_result = resp["words_result"]
            data += f"车牌颜色: {words_result['color']}\n"
            data += f"车牌号: {words_result['number']}"
        return data

    def form(self, file):
        """ 表格文字识别 """
        if file == "":
            return ""
        resp = self.client.form(self.getFileContent(file))
        print(resp)
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            if len(resp["forms_result"]) == 0:
                return data
            forms_result = resp["forms_result"][0]
            # 表头
            data += f"【表头】："
            for header in forms_result["header"]:
                data += f"{header['words']}，"
            # 内容
            data += f"【内容】："
            for body in forms_result["body"]:
                data += f"{body['words']}（{body['row']},{body['column']}），"
        return data

    def receipt(self, file):
        """ 通用票据识别 """
        if file == "":
            return ""
        resp = self.client.receipt(self.getFileContent(file))
        data = ''
        if "error_code" in resp.keys() and resp["error_code"] != 0:
            data = resp["error_msg"]
        else:
            words_result = resp["words_result"]
            for word in words_result:
                data += f"{word['words']}，"
        return data



