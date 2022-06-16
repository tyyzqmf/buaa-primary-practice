import PySimpleGUI as sg


class View:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):

        # window = sg.Window("rect on image", layout)
        # window.Finalize()
        #
        # graph = window.Element("graph")
        #
        # graph.DrawImage(filename="foo.png", location=(0, 400))
        # graph.DrawRectangle((200, 200), (250, 300), line_color="red")
        f1 = sg.Frame(title='通用图像分析',
                      layout=[
                          [sg.Graph(
                              canvas_size=(250, 250),
                              graph_bottom_left=(0, 0),
                              graph_top_right=(250, 250),
                              key="-图片1-"
                          )],
                          # [sg.Image(key='-图片1-', size=(250, 250), background_color='grey')],
                          [sg.InputText(key='-图片1-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入图片1")],
                          [sg.Checkbox('检测人脸', key='-检测人脸-')],
                          [sg.Button("开始识别", key='-开始识别-')],
                          [sg.T("识别结果：")],
                          [sg.Text(key='-图片1-识别结果-', size=(40, 15),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f2 = sg.Frame(title='细粒度图像识别',
                      layout=[
                          [sg.Graph(
                              canvas_size=(250, 250),
                              graph_bottom_left=(0, 0),
                              graph_top_right=(250, 250),
                              key="-图片2-"
                          )],
                          [sg.InputText(key='-图片2-文件-', visible=False, enable_events=True),
                           sg.FileBrowse(button_text="载入图片2")],
                          [sg.Button("菜品识别", key='-菜品识别-'),
                           sg.Button("车型识别", key='-车型识别-'),
                           sg.Button("商标识别", key='-商标识别-')],
                          [sg.Button("动物识别", key='-动物识别-'),
                           sg.Button("植物识别", key='-植物识别-')],
                          [sg.T("识别结果：")],
                          [sg.Text(key='-图片2-识别结果-', size=(40, 15),
                                   text_color="black", background_color="white")]
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [
            [
                f1,
                f2
            ]
        ]

        return sg.Window('图像识别演示', self.main_layout, finalize=True, default_element_size=(50, 1))

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
