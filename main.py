import PySimpleGUI as sg
import functions

First_Operand = None
Operator = None
Second_Operand = None
Result = None


layout = [[sg.InputText("", key='arith_ope', size=(31, 1), disabled=True)],
          [sg.InputText("", key='input_box', size=(31, 1), disabled=True),]]

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "*"],
    ["3", "2", "1", "/"],
    ["C", "0", "=", "-"]
]

for row in buttons:
    row_layout = []
    for button_label in row:
        row_layout.append(sg.Button(button_label, size=(5, 2)))
    layout.append(row_layout)

window = sg.Window('Simple Calculator', layout)

while True:
    event, values = window.read()
    num_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    arith_symbols = ["+", "-", "*", "/"]
    if event in num_symbols:
        functions.get_operands(window, values, event)
    elif event in arith_symbols:
        operand = values['input_box']
        functions.display_operation(window, operand, event)
    elif event == "=":
        # Split first operand to operator
        first_operand = values['arith_ope']
        first_ope = first_operand[:-1].strip()
        operator = first_operand[-1]

        functions.solve_operation(window, first_ope, operator, values)
    elif event == "C":
        First_Operand = None
        Second_Operand = None
    elif event == sg.WIN_CLOSED:
        break

    
window.close()
