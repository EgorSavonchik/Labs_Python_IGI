import Constant

def Calculate(num1, num2, operation):
    match operation:
        case Constant.ADD:
            return (num1 + num2)
        case Constant.SUB:
            return (num1 - num2)
        case Constant.MULT:
            return (num1 * num2)
        case Constant.DIV: 

            if(num2 == 0):
                print("Divide by zero")
                return

            return (num1 / num2)
        case _:
            print("incorrect operation")
