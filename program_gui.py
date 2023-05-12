import PySimpleGUI as sg

layout = [
    [sg.Text('Ingresar texto:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('+', key='-ADD-'), sg.Button('Submit', key='-SUBMIT-')],
    [sg.Text('', key='-OUTPUT-')]
]

window = sg.Window('Ventana con TextBox y Botón', layout)

text_list = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-ADD-':
        text = values['-INPUT-']
        text_list.append(text)
        window['-OUTPUT-'].update(text)
    elif event == '-SUBMIT-':
        text = ', '.join(text_list)
        sg.popup('Textos agregados:', text)

    window['-INPUT-'].update('')

window.close()

window.close()