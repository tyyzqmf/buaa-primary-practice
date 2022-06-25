import PySimpleGUI as sg
import AipBodyAnalysis
import view
import MyImage

if __name__ == "__main__":
    # 创建计算器对象
    view = view.View()
    # 初始化主窗口
    window_main = None
    # 初始化login窗口
    window_login = view.GetLoginWindow()
    # 创建Aip对象
    bodyAnalysis = AipBodyAnalysis.BodyAnalysis()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = bodyAnalysis.login(
                    appid=value["-APP_ID-"],
                    apikey=value["-API_KEY-"],
                    secretkey=value["-SECRET_KEY-"]
                )
                if res:
                    # 登陆成功
                    if not window_main:
                        window_main = view.GetMainWindow()
                        window_main.Finalize()
                    else:
                        window_main.close()
                        window_main = None
                    window_login.close()
                    window_login = None
                else:
                    # 登陆失败
                    window_login["-INFO-"].update("认证错误，请校验：APP_ID，API_KEY，SECRET_KEY")
        elif event == '-图片1-文件-':
            graph = window.Element("-图片1-")
            image = MyImage.MyImage(value['-图片1-文件-'], (300, 500))
            image.deal()
            graph.DrawImage(filename=image.dealname, location=(0, 500))
        elif event == '-关键点识别-':
            image = MyImage.MyImage(value['-图片1-文件-'], (300, 500))
            image.deal()
            body_parts = bodyAnalysis.bodyAnalysis(value['-图片1-文件-'])
            # 画出关键点
            graph = window.Element("-图片1-")
            for key, value in body_parts.items():
                graph.DrawPoint(
                    (int(value["x"] * image.scale), 500 - int(value["y"] * image.scale)),
                    size=8,
                    color="red"
                )
        elif event == '-图片2-文件-':
            graph = window.Element("-图片2-")
            image = MyImage.MyImage(value['-图片2-文件-'], (400, 250))
            image.deal()
            graph.DrawImage(filename=image.dealname, location=(0, 250))
        elif event == '-人流量统计-':
            num, image = bodyAnalysis.bodyNum(value['-图片2-文件-'])
            im = MyImage.MyImage(value['-图片2-文件-'], (400, 250))
            im.base64ToImage(image)
            dealImage = MyImage.MyImage(im.dealname, (400, 250))
            dealImage.deal()
            window_main["-流量-"].update(f"流量：{num}")
            graph = window.Element("-图片2-")
            graph.DrawImage(filename=dealImage.dealname, location=(0, 250))
        elif event == '-图片3-文件-':
            graph = window.Element("-图片3-")
            image = MyImage.MyImage(value['-图片3-文件-'], (200, 200))
            image.deal()
            graph.DrawImage(filename=image.dealname, location=(0, 200))
        elif event == '-手势识别-':
            data = bodyAnalysis.gesture(value['-图片3-文件-'])
            window_main["-手势识别结果-"].update(data)
