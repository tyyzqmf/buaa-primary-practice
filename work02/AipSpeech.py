from aip import AipSpeech


class Aip:
    def __init__(self):
        """ 你的 APPID AK SK """
        APP_ID = '你的 App ID'
        API_KEY = '你的 Api Key'
        SECRET_KEY = '你的 Secret Key'

        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

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
