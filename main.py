import PySimpleGUI as Sg

window = Sg.Window('Simple Calculator',
                   layout=[[Sg.InputText("0", key='input_box', size=(31, 1))],
                           [Sg.Button("+", size=(5, 2)),
                            Sg.Button("*", size=(5, 2)),
                            Sg.Button("/", size=(5, 2)),
                            Sg.Button("-", size=(5, 2))],
                           [Sg.Button("7", size=(5, 2)),
                            Sg.Button("8", size=(5, 2)),
                            Sg.Button("9", size=(5, 2)),
                            Sg.Button("CE", size=(5, 2))],
                           [Sg.Button("4", size=(5, 2)),
                            Sg.Button("5", size=(5, 2)),
                            Sg.Button("6", size=(5, 2)),
                            Sg.Button("C", size=(5, 2))],
                           [Sg.Button("1", size=(5, 2)),
                            Sg.Button("2", size=(5, 2)),
                            Sg.Button("3", size=(5, 2)),
                            Sg.Button("=    ", size=(5, 2))]])

while True:
    event, values = window.read()
    match event:
        case "+":
            window['input_box'].update(event)
        case "*":
            window['input_box'].update(event)
        case "/":
            window['input_box'].update(event)
        case "-":
            window['input_box'].update(event)
        case "0":
            ope1 = values['input_box'].strip()
            ope1 += event
            window['input_box'].update(ope1)
        case "1":
            ope1 = values['input_box'].strip()
            ope1 += event
            window['input_box'].update(ope1)
        case "2":
            ope1 = values['input_box'].strip()
            ope1 += event
            window['input_box'].update(ope1)
        case "3":
            ope1 = values['input_box'].strip()
            ope1 += event
            window['input_box'].update(ope1)
        case "4":
            window['input_box'].update(event)
        case "5":
            window['input_box'].update(event)
        case "6":
            window['input_box'].update(event)
        case "7":
            window['input_box'].update(event)
        case "8":
            window['input_box'].update(event)
        case "9":
            window['input_box'].update(event)
        case Sg.WIN_CLOSED:
            break
    print(values)
    print(event)
    print(ope1)
window.close()
