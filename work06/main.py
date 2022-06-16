import PySimpleGUI as sg
import AipImageClassify
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
    imageClassify = AipImageClassify.ImageClassify()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = imageClassify.login(
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
            image = MyImage.MyImage(value['-图片1-文件-'])
            image.deal()
            graph.DrawImage(filename=image.dealname, location=(0, 250))
        elif event == '-开始识别-':
            with_face = 0
            if value['-检测人脸-']:
                with_face = 1
            data, p1, p2 = imageClassify.threadPoolClassify(value['-图片1-文件-'], with_face)
            graph = window.Element("-图片1-")
            graph.DrawRectangle(p1, p2, line_color="red")
            window_main["-图片1-识别结果-"].update(data)
        elif event == '-图片2-文件-':
            graph = window.Element("-图片2-")
            image = MyImage.MyImage(value['-图片2-文件-'])
            image.deal()
            graph.DrawImage(filename=image.dealname, location=(0, 250))
        elif event == '-菜品识别-':
            data = imageClassify.dishDetect(value['-图片2-文件-'])
            window_main["-图片2-识别结果-"].update(data)
        elif event == '-车型识别-':
            data = imageClassify.carDetect(value['-图片2-文件-'])
            window_main["-图片2-识别结果-"].update(data)
        elif event == '-商标识别-':
            data = imageClassify.logoSearch(value['-图片2-文件-'])
            window_main["-图片2-识别结果-"].update(data)
        elif event == '-动物识别-':
            data = imageClassify.animalDetect(value['-图片2-文件-'])
            window_main["-图片2-识别结果-"].update(data)
        elif event == '-植物识别-':
            data = imageClassify.plantDetect(value['-图片2-文件-'])
            window_main["-图片2-识别结果-"].update(data)
