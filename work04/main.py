import PySimpleGUI as sg
from PIL import Image, ImageTk
import AipFace
import view


# 处理图片
def DealImage(filename):
    # Resize PNG file to size
    size = (150, 200)
    im = Image.open(filename).convert('RGB')
    im = im.resize(size, resample=Image.BICUBIC)
    # Convert im to ImageTk.PhotoImage
    image = ImageTk.PhotoImage(image=im)
    return image


if __name__ == "__main__":
    # 创建计算器对象
    view = view.View()
    # 初始化主窗口
    window_main = None
    # 初始化login窗口
    window_login = view.GetLoginWindow()
    # 创建Aip对象
    face = AipFace.Face()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = face.login(
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
        elif event == '-人脸1-文件-':
            image = DealImage(value['-人脸1-文件-'])
            window['-人脸1-图片-'].update(data=image)
            data = face.detect(value['-人脸1-文件-'])
            window_main["-人脸1检测结果-"].update(data)
        elif event == '-人脸2-文件-':
            image = DealImage(value['-人脸2-文件-'])
            window['-人脸2-图片-'].update(data=image)
            data = face.detect(value['-人脸2-文件-'])
            window_main["-人脸2检测结果-"].update(data)
        elif event == '人脸对比':
            data = face.match(value['-人脸1-文件-'], value['-人脸2-文件-'])
            window_main["-人脸对比-结果-"].update(data)
