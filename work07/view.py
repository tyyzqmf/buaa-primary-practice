import PySimpleGUI as sg


class View:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='关键点识别',
                      layout=[
                          [sg.InputText(key='-图片1-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入图片1"),
                           sg.Button("关键点识别", key='-关键点识别-')],
                          [sg.Graph(
                              canvas_size=(300, 500),
                              graph_bottom_left=(0, 0),
                              graph_top_right=(300, 500),
                              key="-图片1-"
                          )],
                      ],
                      )
        f2 = sg.Frame(title='人流量统计',
                      layout=[
                          [sg.InputText(key='-图片2-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入图片2"),
                           sg.Button("人流量统计", key='-人流量统计-'),
                           sg.T("流量：", key='-流量-')],
                          [sg.Graph(
                              canvas_size=(400, 250),
                              graph_bottom_left=(0, 0),
                              graph_top_right=(400, 250),
                              key="-图片2-"
                          )],
                      ],
                      )
        f3 = sg.Frame(title='手势识别',
                      layout=[
                          [sg.InputText(key='-图片3-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入图片3"),
                           sg.Button("手势识别", key='-手势识别-')],
                          [
                              sg.Graph(
                                  canvas_size=(200, 200),
                                  graph_bottom_left=(0, 0),
                                  graph_top_right=(200, 200),
                                  key="-图片3-"
                              ),
                              sg.Column(
                                  [
                                      [sg.T("识别结果：")],
                                      [sg.Text(key='-手势识别结果-', size=(20, 15),
                                               text_color="black", background_color="white")]
                                  ]),
                          ],
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [
            [
                f1,
                sg.Column([[f2], [f3]]),
            ]
        ]

        return sg.Window('人体分析演示', self.main_layout, finalize=True, default_element_size=(50, 1))

    # 创建登陆窗口
    def GetLoginWindow(self, ):
        # 定义布局
        self.login_layout = [
            [sg.T("APP_ID：", size=(13, 1)), sg.InputText(key='-APP_ID-', default_text="26543735")],
            [sg.T("API_KEY：", size=(13, 1)), sg.InputText(key='-API_KEY-', default_text="isG9e3IIytIs8qCRTcWnWXSb")],
            [sg.T("SECRET_KEY：", size=(13, 1)),
             sg.InputText(key='-SECRET_KEY-', default_text="IjF48hMSBy3eQPdZT5iTqGnftu1mURr4")],
            [sg.T("", key='-INFO-', text_color="red")],
            [sg.Button("登陆")]
        ]

        return sg.Window('登陆', self.login_layout, finalize=True, default_element_size=(50, 1))
