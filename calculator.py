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

    elif choice == 3:
        return num1 * num2  

    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    elif choice == 5:
        return num1 % num2 

    elif choice == 6:
        return num1 ** num2 
    
   
   


# Calling Menu
menu()

choice=""

try:
    # Getting input of selection of menu item.
    choice = int(input("Enter Your Choice = "))

    #checks choice is in range 1 to 6
    if choice < 1 or choice > 6:
        raise Exception()

except ValueError:
    print("Enter integer value in choice !")

except:
    print("You entered wrong choice !")

else:
    # Getting inputs of two numbers.
    num1 = eval(input("Enter num 1 = "))
    num2 = eval(input("Enter num 2 = "))

    # Passing parameters in calculate method and print return value
    print(calculate(choice, num1, num2))
