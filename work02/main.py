import PySimpleGUI as sg
from work02.AipSpeech import Aip


class Voice:
    def __init__(self):
        # 变量
        self.result = '0'
        self.history_list = []
        self.main_layout = []

    # 创建主窗口
    def GetMainWindow(self, ):
        f1 = sg.Frame(title='语音识别',
                      layout=[
                          [sg.InputText(key='-file-'), sg.FileBrowse(button_text="选择文件")],
                          [
                              sg.T("音频格式："),
                              sg.Combo(key='-type-', values=['pcm', 'wav', 'amr'], default_value='pcm'),
                              sg.Button("开始识别")
                          ],
                          [sg.T("识别结果：")],
                          [sg.Text(key='-result-', text="", size=(50, 5), text_color="black", background_color="white")],
                      ],
                      )
        f2 = sg.Frame(title='语音合成',
                      layout=[
                          [sg.Multiline(key='-content-', size=(40, 10))],
                          [sg.Button("开始合成")],
                      ],
                      )
        # 定义主窗口布局
        self.main_layout = [[f1, f2]]

        return sg.Window('语音演示', self.main_layout, finalize=True, default_element_size=(50, 1))


if __name__ == "__main__":
    # 创建计算器对象
    voice = Voice()
    # 初始化主窗口
    window_main = voice.GetMainWindow()
    # 创建Aip对象
    aip = Aip()

    while True:
        window, event, value = sg.read_all_windows()
        if window == window_main and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '开始识别':
            filepath = value["-file-"]
            format = value["-type-"]
            resp = aip.asr(filepath=filepath, format=format)
            result = ''
            if resp['err_no'] != 0:
                result = resp['err_msg']
            else:
                result = resp['result'][0]
            window_main['-result-'].update(result)
        elif event == '开始合成':
            print(value)

    window.close()
