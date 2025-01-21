# Menu for showing operation list
def menu():
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Modulus ")
    print("6. Exponent ")
    
# Calculating Operations
def calculate(choice, num1, num2):
    if choice == 1:
        return num1 + num2

    elif choice == 2:
        return num1 - num2 


    
    

# Calling Menu
menu()

# Getting input of selection of menu item.
choice = int(input("Enter Your Choice = "))

# Getting inputs of two numbers.
num1 = eval(input("Enter num 1 = "))
num2 = eval(input("Enter num 2 = "))

# Passing parameters in calculate method and print return value
print(calculate(choice, num1, num2))
