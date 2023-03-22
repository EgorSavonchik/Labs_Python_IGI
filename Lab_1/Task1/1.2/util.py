import constant

def calculate(num1, num2, operation):
    match operation:
        case constant.ADD:
            return (num1 + num2)
        case constant.SUB:
            return (num1 - num2)
        case constant.MULT:
            return (num1 * num2)
        case constant.DIV: 

            if(num2 == 0):
                print("Divide by zero")
                return

            return (num1 / num2)
        case _:
            print("incorrect operation")
