import PySimpleGUI as sg


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
                          [sg.Text(text="111111", size=(50, 5), text_color="black", background_color="white")],
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
    express = '0'
    flag = 0

    while True:
        window, event, value = sg.read_all_windows()
        if window == window_main and event in (None, sg.WIN_CLOSED):
            window.close()
        elif event == '开始识别':
            print(value)
        elif event == '开始合成':
            print(value)

    window.close()
