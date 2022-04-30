import PySimpleGUI as sg
import AipNlp
import view


if __name__ == "__main__":
    # 创建计算器对象
    view = view.View()
    # 初始化主窗口
    window_main = None
    # 初始化login窗口
    window_login = view.GetLoginWindow()
    # 创建Aip对象
    nlp = AipNlp.Nlp()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = nlp.login(
                    appid=value["-APP_ID-"],
                    apikey=value["-API_KEY-"],
                    secretkey=value["-SECRET_KEY-"]
                )
                if res:
                    # 登陆成功
                    if not window_main:
                        window_main = view.GetMainWindow()
                    else:
                        window_main.close()
                        window_main = None
                    window_login.close()
                    window_login = None
                else:
                    # 登陆失败
                    window_login["-INFO-"].update("认证错误，请校验：APP_ID，API_KEY，SECRET_KEY")
        elif event == '词法分析':
            data = nlp.lexer(value["-词法分析-输入-"])
            window_main["-词法分析-表-"].update(data)
        elif event == '依存句法分析':
            data = nlp.depParser(value["-词法分析-输入-"])
            window_main["-依存句法分析-表-"].update(data)
        elif event == 'DNN语言模型':
            data, ppl = nlp.dnnlm(value["-词法分析-输入-"])
            window_main["-DNN语言模型-表-"].update(data)
            window_main["-句子通顺值-"].update(ppl)
        elif event == '文本相似度':
            data = nlp.simnet(value["-短文本相似度-文本1-"], value["-短文本相似度-文本2-"])
            window_main["-短文本相似度-结果-"].update(data)
        elif event == '评论观点抽取':
            data = nlp.commentTag(value["-评论内容-"], value["-评论类型-"])
            window_main["-评论结果-"].update(data)
        elif event == '情感倾向分析':
            data = nlp.sentimentClassify(value["-评论内容-"])
            window_main["-评论结果-"].update(data)
        elif event == '词向量':
            data = nlp.wordEmbedding(value["-词向量-输入-"])
            window_main["-词向量结果-"].update(data)
        elif event == '词义相似度':
            data = nlp.wordSimEmbedding(value["-词义相似度-词一-"], value["-词义相似度-词二-"])
            window_main["-词义相似度-结果-"].update(data)
        elif event == '文章标签':
            data = nlp.keyword(value["-文章标题-"], value["-文章内容-"])
            window_main["-标签/分类结果-"].update(data)
        elif event == '文章分类':
            data = nlp.topic(value["-文章标题-"], value["-文章内容-"])
            window_main["-标签/分类结果-"].update(data)

