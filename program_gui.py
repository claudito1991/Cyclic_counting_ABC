import PySimpleGUI as sg

layout = [
    [[sg.Text('Ingresar feriado:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Agregar feriado', key='-ADD-'), sg.Button('Aceptar', key='-SUBMIT-')],
    [sg.Text('', key='-OUTPUT-')]],

    [[sg.Text('Ingresar archivo ABC:')],
    [sg.FileBrowse(key='-ABC-FILE-')],
    [sg.Button('Procesar', key='-PROCESS-'), sg.Button('Cancelar', key='-CANCEL-')],
    [sg.Text('', key='-OUTPUT-PROCESS-')]]
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
