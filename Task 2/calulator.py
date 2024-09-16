def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    else:
        return x / y

def calculate():
    print("Enter 1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                x = float(input("Enter number 1:\n"))
                y = float(input("Enter number 2:\n"))
                
            except ValueError:
                print("Enter valid input")
                continue

            if choice == '1':
                print(f"{x} + {y} = {add(x, y)}")

            elif choice == '2':
                print(f"{x} - {y} = {subtract(x, y)}")
            
            elif choice == '3':
                print(f"{x} * {y} = {multiply(x, y)}")
            
            elif choice == '4':
                if y == 0:
                    print("Division by zero is not possible")
                else:
                    print(f"{x} / {y} = {divide(x, y)}")

            continuation  = input("Enter 5 to exit or any other key to continue: ")
            if continuation == '5':
                print("Program terminated")
                break

        else:
            print("Invalid choice!")

calculate()
