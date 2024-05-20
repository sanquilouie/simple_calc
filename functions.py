def get_operands(window, values, event):
    operand = values['input_box']
    operand += event
    window['input_box'].update(operand)


def display_operation(window, operand, event):
    window['arith_ope'].update(operand + " " + event)


def solve_operation(window, first_ope, operator, values):
    result = first_ope + " " + operator + " " + values['input_box']
    print(result)
    window['arith_ope'].update(result + " =")
    window['input_box'].update(eval(result))
