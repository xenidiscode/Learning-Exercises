def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

prakseis = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
cont_inue = ['y', 'n', 'over']
def calculator():

    from art import logo
    print(logo)

    calculator_over = True
    first_calc = True
    while calculator_over:
        if first_calc:
            first_number = float(input("What's the first number?: "))
        for key in prakseis:
            print(key)

        operation_input = input("Pick an operation?: ")
        while operation_input not in prakseis:
            print("Please provide an operation symbol from the ones previously shown: '+', '-', '*', '/'. ")
            operation_input = input("Pick an operation?: ")

        second_number = float(input("What's the next number: "))
        result = prakseis[operation_input](first_number, second_number)
        print(f"{first_number} {operation_input} {second_number} = {result}")

        new_calc = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'over' to end Pythonista: ")
        while new_calc not in cont_inue:
            print("Please provide a valid answer. 'y' for yes or 'n' for no")
            new_calc = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'over' to end Pythonista: ")

        if new_calc == 'y':
            first_number = result
            first_calc = False
        elif new_calc == 'over':
            calculator_over = False
        else:
            print("\n"*20)
            calculator()
calculator()