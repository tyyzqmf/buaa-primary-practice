import PySimpleGUI as sg


# 定义主窗口布局，确定行数
def window_main():
    layout = [
        [sg.Text('计算结果：', font=("微软雅黑", 10)), sg.Button('历史记录', font=("微软雅黑", 10), pad=(10, 1))],
        [sg.Text('0', key='-express-', justification='right', size=(30, 1), font=("微软雅黑", 10), background_color='#fff',
                 text_color='#000')],
        [sg.Text('0', key='-result-', justification='right', size=(30, 1), font=("微软雅黑", 10), background_color='#fff',
                 text_color='#000')],
        [sg.Button('清空', size=(6, 2)), sg.Button('删除', size=(6, 2)), sg.Button('x²', size=(6, 2)),
         sg.Button('÷', size=(6, 2))],
        [sg.Button('7', size=(6, 2)), sg.Button('8', size=(6, 2)), sg.Button('9', size=(6, 2)),
         sg.Button('x', size=(6, 2))],
        [sg.Button('4', size=(6, 2)), sg.Button('5', size=(6, 2)), sg.Button('6', size=(6, 2)),
         sg.Button('-', size=(6, 2))],
        [sg.Button('1', size=(6, 2)), sg.Button('2', size=(6, 2)), sg.Button('3', size=(6, 2)),
         sg.Button('+', size=(6, 2))],
        [sg.Button('+/-', size=(6, 2)), sg.Button('0', size=(6, 2)), sg.Button('.', size=(6, 2)),
         sg.Button('=', size=(6, 2))],
    ]

    # 创建窗口
    return sg.Window('简易计算器@月亮', layout, finalize=True, default_element_size=(50, 1))


# 定义历史记录窗口布局
def createwindow_history(history_list=None):
    history_text = ''
    if history_list:
        history_text = '\n'.join(['='.join(i) for i in history_list])
    layout = [
        [sg.Text('历史记录：', font=("微软雅黑", 10))],
        [sg.Multiline(history_text, justification='right', disabled=True, autoscroll=True, size=(30, 10),
                      font=("微软雅黑", 10), background_color='#fff', text_color='#000')]
    ]
    return sg.Window('历史记录', layout, finalize=True)


def get_result(eval_str):
    global result
    eval_str = eval_str.replace('^', '**').replace('x', '*').replace('÷', '/')
    try:
        result = eval(eval_str)
    except Exception as e:
        result = '0'
    window_main['-result-'].update(result)
    return str(result)


window_main = window_main()
window_sub = None
history_list = []
express = '0'
result = '0'
flag = 0

while True:
    window, event, value = sg.read_all_windows()
    if window == window_main and event in (None, sg.WIN_CLOSED):
        if window_sub is not None:
            window_sub.close()
        break
    elif event == '历史记录':
        if not window_sub:
            window_sub = createwindow_history(history_list)
        else:
            window_sub.close()
            window_sub = None
    elif window == window_sub and event is None:
        window_sub.close()
        window_sub = None
    elif event == '=':
        express1 = express
        express = get_result(express)
        history_list.append([express1, express])
        flag = 1
    elif event == '清空':
        express = '0'
        result = '0'
        window_main['-express-'].update(express)
        window_main['-result-'].update(result)
    elif event == '删除':
        if len(express.lstrip('-').strip('(').strip(')')) == 1:
            express = '0'
        elif express[-1] == ')':
            express = express.lstrip('-').strip('(').strip(')')
        else:
            express = express[:-1]
        window_main['-express-'].update(express)
    elif event == 'x²':
        express = f'({express}) ^ 2'
        window_main['-express-'].update(express)
    elif event == '+/-':
        express = f'-({express})'
        get_result(express)
    else:
        if flag == 1 and event in '0123456789':
            express = '0'
            flag = 0
        if express == '0':
            express = event
        else:
            express = express + event
        window_main['-express-'].update(express)

window.close()
