import util

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except:
    print("Incorrect number")
    exit()

print(util.calculate(num1, num2, input("Enter operation: ")))