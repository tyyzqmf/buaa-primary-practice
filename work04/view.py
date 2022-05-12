import PySimpleGUI as sg


class View:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='人脸1',
                      layout=[
                          [sg.Image(key='-人脸1-图片-', size=(150, 200), background_color='grey')],
                          [sg.InputText(key='-人脸1-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入人脸1")],
                          [sg.T("人脸1检测结果：")],
                          [sg.Text(key='-人脸1检测结果-', size=(25, 12),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f2 = sg.Frame(title='对比',
                      layout=[
                          [sg.Button("人脸对比")],
                          [sg.T("对比结果：")],
                          [sg.Text(key='-人脸对比-结果-', size=(15, 4),
                                   text_color="black", background_color="white")],
                      ],
                      )
        f3 = sg.Frame(title='人脸2',
                      layout=[
                          [sg.Image(key='-人脸2-图片-', size=(150, 200), background_color='grey')],
                          [sg.InputText(key='-人脸2-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入人脸2")],
                          [sg.T("人脸2检测结果：")],
                          [sg.Text(key='-人脸2检测结果-', size=(25, 12),
                                   text_color="black", background_color="white")]
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [
            [
                f1,
                f2,
                f3
            ]
        ]

        return sg.Window('人脸识别演示', self.main_layout, finalize=True, default_element_size=(50, 1))

    # 创建登陆窗口
    def GetLoginWindow(self, ):
        # 定义布局
        self.login_layout = [
            [sg.T("APP_ID：", size=(13, 1)), sg.InputText(key='-APP_ID-', default_text="")],
            [sg.T("API_KEY：", size=(13, 1)), sg.InputText(key='-API_KEY-', default_text="")],
            [sg.T("SECRET_KEY：", size=(13, 1)),
             sg.InputText(key='-SECRET_KEY-', default_text="")],
            [sg.T("", key='-INFO-', text_color="red")],
            [sg.Button("登陆")]
        ]

        return sg.Window('登陆', self.login_layout, finalize=True, default_element_size=(50, 1))
