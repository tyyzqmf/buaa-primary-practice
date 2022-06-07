import PySimpleGUI as sg


class View:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='通用文字识别',
                      layout=[
                          [sg.Radio('普通精度', "精度", default=True, key='-普通精度-'),
                           sg.Radio('高精度', "精度", default=False, key='-高精度-')],
                          [sg.Checkbox('含位置信息', key='-含位置信息-'),
                           sg.Checkbox('检测方向', key='-检测方向-')],
                          [sg.Button("识别图片", key='-通用文字识别-识别图片-')],
                          [sg.Text(key='-通用文字识别-结果-', size=(35, 12),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f2 = sg.Frame(title='网络图片文字识别',
                      layout=[
                          [sg.Button("识别图片", key='-网络图片文字识别-识别图片-')],
                          [sg.Text(key='-网络图片文字识别-结果-', size=(35, 12),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f3 = sg.Frame(title='卡证识别',
                      layout=[
                          [sg.Radio('身份证正面', "卡证", default=True, key='-身份证正面-'),
                           sg.Radio('身份证背面', "卡证", default=False, key='-身份证背面-'),
                           sg.Radio('银行卡', "卡证", default=False, key='-银行卡-'),
                           sg.Radio('营业执照', "卡证", default=False, key='-营业执照-')],
                          [sg.Radio('驾驶证', "卡证", default=False, key='-驾驶证-'),
                           sg.Radio('行驶证', "卡证", default=False, key='-行驶证-'),
                           sg.Radio('车牌', "卡证", default=False, key='-车牌-')],
                          [sg.Button("识别图片", key='-卡证识别-识别图片-')],
                          [sg.Text(key='-卡证识别-结果-', size=(50, 6),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f4 = sg.Frame(title='表格文字识别',
                      layout=[
                          [sg.Button("识别图片", key='-表格文字识别-识别图片-')],
                          [sg.Text(key='-表格文字识别-结果-', size=(50, 6),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f5 = sg.Frame(title='通用票据识别',
                      layout=[
                          [sg.Button("识别图片", key='-通用票据识别-识别图片-')],
                          [sg.Text(key='-通用票据识别-结果-', size=(50, 6),
                                   text_color="black", background_color="white")]
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [
            [
                [sg.InputText(key='-选择图片-', size=(85, 12)), sg.FileBrowse(button_text="选择图片")],
                sg.Column([[f1], [f2]]),
                sg.Column([[f3], [f4], [f5]]),
            ]
        ]

        return sg.Window('文字识别演示', self.main_layout, finalize=True, default_element_size=(50, 1))

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
