from aip import AipSpeech


class Aip:
    def __init__(self):
        self.client = None

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipSpeech(appid, apikey, secretkey)
        # 校验密钥是否正确
        try:
            authObj = self.client._auth()
            params = self.client._getParams(authObj)
            return True
        except Exception as e:
            return False

    # 语音识别
    def asr(self, filepath, format='pcm', rate=16000):
        # 读取文件
        def get_file_content(path):
            with open(path, 'rb') as fp:
                return fp.read()

        # 识别本地文件
        return self.client.asr(get_file_content(filepath), format, rate, {
            'dev_pid': 1537,
        })

    # 语音合成
    def synthesis(self, text, lang='zh', ctp=1, options=None):
        result = self.client.synthesis(text, 'zh', 1, {
            'vol': 5,
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)
