import PySimpleGUI as sg
import AipSpeech


class Voice:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='语音识别',
                      layout=[
                          [sg.InputText(key='-file-'), sg.FileBrowse(button_text="选择文件")],
                          [
                              sg.T("音频格式："),
                              sg.Combo(key='-type-', values=['pcm', 'wav', 'amr'], default_value='pcm'),
                              sg.Button("开始识别")
                          ],
                          [sg.T("识别结果：")],
                          [sg.Text(key='-result-', text="", size=(50, 5),
                                   text_color="black", background_color="white")],
                      ],
                      )
        f2 = sg.Frame(title='语音合成',
                      layout=[
                          [sg.Multiline(key='-content-', size=(40, 10))],
                          [sg.Button("开始合成")],
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [[f1, f2]]

        return sg.Window('语音演示', self.main_layout, finalize=True, default_element_size=(50, 1))

    # 创建登陆窗口
    def GetLoginWindow(self, ):
        # 定义布局
        self.login_layout = [
            [sg.T("APP_ID：", size=(13, 1)), sg.InputText(key='-APP_ID-')],
            [sg.T("API_KEY：", size=(13, 1)), sg.InputText(key='-API_KEY-')],
            [sg.T("SECRET_KEY：", size=(13, 1)), sg.InputText(key='-SECRET_KEY-')],
            [sg.T("", key='-INFO-', text_color="red")],
            [sg.Button("登陆")]
        ]

        return sg.Window('登陆', self.login_layout, finalize=True, default_element_size=(50, 1))


if __name__ == "__main__":
    # 创建计算器对象
    voice = Voice()
    # 初始化主窗口
    window_main = None
    # 初始化login窗口
    window_login = voice.GetLoginWindow()
    # 创建Aip对象
    aip = AipSpeech.Aip()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '开始识别':
            filepath = value["-file-"]
            format = value["-type-"]
            resp = aip.asr(filepath=filepath, format=format)
            result = ''
            if resp['err_no'] != 0:
                result = resp['err_msg']
            else:
                result = resp['result'][0]
            window_main['-result-'].update(result)
        elif event == '开始合成':
            content = value["-content-"]
            aip.synthesis(text=content)
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = aip.login(
                    appid=value["-APP_ID-"],
                    apikey=value["-API_KEY-"],
                    secretkey=value["-SECRET_KEY-"]
                )
                if res:
                    # 登陆成功
                    if not window_main:
                        window_main = voice.GetMainWindow()
                    else:
                        window_main.close()
                        window_main = None
                    window_login.close()
                    window_login = None
                else:
                    # 登陆失败
                    window_login["-INFO-"].update("认证错误，请校验：APP_ID，API_KEY，SECRET_KEY")

    window.close()
