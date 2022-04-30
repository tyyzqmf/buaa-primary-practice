import PySimpleGUI as sg


class View:
    def __init__(self):
        # 变量
        self.main_layout = []
        self.login_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='词法分析/依存句法分析/DNN语言模型',
                      layout=[
                          [sg.InputText(key='-词法分析-输入-', size=(40, 1), default_text="我们在北航学习人工智能")],
                          [sg.Button("词法分析")],
                          [sg.Table(
                              key='-词法分析-表-',
                              values=[["    ", "       ", "        ", "           "]],
                              headings=['序号', '分词', '词性', '基本词'],
                              hide_vertical_scroll=True,
                              auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
                              justification='center',  # 字符排列 left right center
                              num_rows=6,  # 行数
                              text_color='black',
                              background_color='white')],
                          [sg.Button("依存句法分析")],
                          [sg.Table(
                              key='-依存句法分析-表-',
                              values=[["   ", "       ", "       ", "       ", "       "]],
                              headings=['序号', '词', '词性', '依赖词', '依存关系'],
                              hide_vertical_scroll=True,
                              auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
                              justification='center',  # 字符排列 left right center
                              num_rows=6,  # 行数
                              text_color='black',
                              background_color='white')],
                          [
                              sg.Button("DNN语言模型"),
                              sg.T("句子通顺值："),
                              sg.Text(key='-句子通顺值-', size=(10, 1),
                                      text_color="black", background_color="white"),
                          ],
                          [sg.Table(
                              key='-DNN语言模型-表-',
                              values=[["        ", "        ", "               "]],
                              headings=['序号', '分词', '概率值'],
                              hide_vertical_scroll=True,
                              auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
                              justification='center',  # 字符排列 left right center
                              num_rows=6,  # 行数
                              text_color='black',
                              background_color='white')],
                      ],
                      )
        f2 = sg.Frame(title='短文本相似度',
                      layout=[
                          [sg.Multiline(key='-短文本相似度-文本1-', size=(25, 4), no_scrollbar=True,
                                        default_text="我们在北航学习人工智能"),
                           sg.Multiline(key='-短文本相似度-文本2-', size=(25, 4), no_scrollbar=True,
                                        default_text="学习人工智能")],
                          [sg.Button("文本相似度"),
                           sg.T("结果："),
                           sg.Text(key='-短文本相似度-结果-', size=(10, 1),
                                   text_color="black", background_color="white")],
                      ],
                      )
        f3 = sg.Frame(title='评论观点抽取/情感倾向分析',
                      layout=[
                          [sg.Multiline(key='-评论内容-', size=(52, 4), no_scrollbar=True,
                                        default_text="三星电脑电池不给力")],
                          [
                              sg.T("行业："),
                              sg.Combo(
                                  key='-评论类型-',
                                  values=["酒店",
                                          "KTV",
                                          "丽人",
                                          "美食餐饮",
                                          "旅游",
                                          "健康",
                                          "教育",
                                          "商业",
                                          "房产",
                                          "汽车",
                                          "生活",
                                          "购物",
                                          "3C"],
                                  size=(10, 1),
                                  default_value='生活'),
                              sg.Button("评论观点抽取"),
                              sg.Button("情感倾向分析")
                          ],
                          [sg.Text(key='-评论结果-', size=(52, 3),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f4 = sg.Frame(title='词向量',
                      layout=[
                          [sg.InputText(key='-词向量-输入-', size=(15, 1), default_text="北航"),
                           sg.Button("词向量")],
                          [sg.Text(key='-词向量结果-', size=(25, 5),
                                   text_color="black", background_color="white")]
                      ],
                      )
        f5 = sg.Frame(title='词义相似度',
                      layout=[
                          [sg.T("词一："),
                           sg.InputText(key='-词义相似度-词一-', size=(15, 1), default_text="北航")],
                          [sg.T("词二："),
                           sg.InputText(key='-词义相似度-词二-', size=(15, 1), default_text="大学")],
                          [sg.Button("词义相似度")],
                          [sg.T("结果："),
                           sg.Text(key='-词义相似度-结果-', size=(15, 1),
                                   text_color="black", background_color="white")],
                      ],
                      )
        f6 = sg.Frame(title='文章标签/文章分类',
                      layout=[
                          [sg.T("文章标题")],
                          [sg.InputText(key='-文章标题-', size=(30, 1),
                                        default_text="欧洲冠军杯足球赛")],
                          [sg.T("文章内容")],
                          [sg.Multiline(key='-文章内容-', size=(30, 11), no_scrollbar=True,
                                        default_text="欧洲冠军联赛是欧洲足球协会联盟主办的年度足球比赛，代表欧洲俱乐部足球最高荣誉和水平，被认为是全世界最高素质、最具影响力以及最高水平的俱乐部赛事，亦是世界上奖金最高的足球赛事和体育赛事之一。")],
                          [sg.Button("文章标签"), sg.Button("文章分类")],
                          [sg.T("标签/分类结果：")],
                          [sg.Text(key='-标签/分类结果-', size=(30, 8),
                                   text_color="black", background_color="white")],
                      ],
                      )
        # 定义主窗口布局
        # 复杂布局用Column
        self.main_layout = [
            [
                f1,
                sg.Column([[f2], [f3], [f4, f5]]),
                f6
            ]
        ]

        return sg.Window('自然语言处理演示', self.main_layout, finalize=True, default_element_size=(50, 1))

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
