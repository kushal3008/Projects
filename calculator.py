print("Welcome to the Calculator")
def addition():
    answer = 0
    a = int(input("Enter how many number u need to add:"))
    for i in range(a):
        b = float(input("Enter values you want to add:"))
        answer += b
        if i == a-1:
            print(f"Answer of the addition is {round(answer,3)}")
def subtraction():
    a = int(input("Enter how many number you need to subtract:"))
    for i in range(a):
        if i == 0:
            b  = float(input("Enter first value of the subtraction:"))
            answer = b
        else:
            b = float(input("Enter values you want to subtract:"))
            answer -= b
            if i == a-1:
                print(f"Answer of the subtraction is {round(answer,3)}")
def multiplication():
    a = int(input("Enter how many number you need to multiply:"))
    answer = 1
    for i in range(a):
        b = float(input("Enter values you want to multiply:"))
        answer *= b
        if i == a - 1:
            print(f"Answer of the multiplication is {round(answer,3)}")
def division():
    a = int(input("Enter how many number you need to divide:"))
    try:
        for i in range(a):
            if i == 0:
                b = float(input("Enter first value of the division:"))
                answer = b
            else:
                b = float(input("Enter values you want to divide:"))
                answer /= b
                if i == a - 1:
                    print(f"Answer of the division is {round(answer,3)}")
    except ZeroDivisionError:
        print("Can't divide Zero")
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    n = int(input("Select an operation:"))
    if n > 5 or n < 1:
        print("!!!Enter a valid option!!!")
    else:
        if n == 5:
            print("Thanks for using Calculator")
        match(n):
            case 1: addition()
            case 2: subtraction()
            case 3: multiplication()
            case 4: division()
            case 5: break