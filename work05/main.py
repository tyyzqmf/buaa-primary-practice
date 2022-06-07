import PySimpleGUI as sg
import AipOcr
import view

if __name__ == "__main__":
    # 创建计算器对象
    view = view.View()
    # 初始化主窗口
    window_main = None
    # 初始化login窗口
    window_login = view.GetLoginWindow()
    # 创建Aip对象
    ocr = AipOcr.Ocr()

    while True:
        window, event, value = sg.read_all_windows()
        if (window == window_main or window == window_login) and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '登陆':
            if not value["-APP_ID-"] or not value["-API_KEY-"] or not value["-SECRET_KEY-"]:
                window_login["-INFO-"].update("APP_ID，API_KEY，SECRET_KEY不能为空")
            else:
                res = ocr.login(
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
        elif event == '-通用文字识别-识别图片-':
            # 参数
            detect_direction = "false"
            if value['-检测方向-']:
                detect_direction = "true"
            precision = "base"
            if value['-高精度-']:
                detect_direction = "high"
            vertexes_location = "false"
            if value['-含位置信息-']:
                vertexes_location = "true"
            # 调用方法
            data = ocr.allGeneral(value['-选择图片-'],
                                  precision=precision,
                                  detect_direction=detect_direction,
                                  vertexes_location=vertexes_location)
            window_main["-通用文字识别-结果-"].update(data)
        elif event == '-网络图片文字识别-识别图片-':
            # 参数
            detect_direction = "false"
            if value['-检测方向-']:
                detect_direction = "true"
            # 调用方法
            data = ocr.webImage(value['-选择图片-'],
                                detect_direction=detect_direction)
            window_main["-网络图片文字识别-结果-"].update(data)
        elif event == '-卡证识别-识别图片-':
            # 调用方法
            if value['-身份证正面-']:
                data = ocr.idCard(value['-选择图片-'], id_card_side="front")
            elif value['-身份证背面-']:
                data = ocr.idCard(value['-选择图片-'], id_card_side="back")
            elif value['-银行卡-']:
                data = ocr.bankCard(value['-选择图片-'])
            elif value['-营业执照-']:
                data = ocr.businessLicense(value['-选择图片-'])
            elif value['-驾驶证-']:
                data = ocr.drivingLicense(value['-选择图片-'])
            elif value['-行驶证-']:
                data = ocr.vehicleLicense(value['-选择图片-'])
            elif value['-车牌-']:
                data = ocr.licensePlate(value['-选择图片-'])
            window_main["-卡证识别-结果-"].update(data)
        elif event == '-表格文字识别-识别图片-':
            # 调用方法
            data = ocr.form(value['-选择图片-'])
            window_main["-表格文字识别-结果-"].update(data)
        elif event == '-通用票据识别-识别图片-':
            # 调用方法
            data = ocr.receipt(value['-选择图片-'])
            window_main["-通用票据识别-结果-"].update(data)

