print("Performed By 43 & 47")

#ZeroDivision
def ZeroDivision():
    try:
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        result = a / b
        print("Division : ", result)
    except ZeroDivisionError:
        print("Value Can't Divide by zero.")

#valueError
def valueError():
    try:
        a = int("abc")
        b = 10 / 0
    except ZeroDivisionError:
        print("Value Can't Divide by zero.")
    except ValueError:
        print("Value cannot be converted..!!")

#TryExceptElse
def TryExceptElse():
    try:
        num = int(input("Enter a number : "))
        print("Valid Number Entered")
    except ValueError:
        print("Invalid Input")
    else:
        print("Square : ", num**2)

#FinalBlock
def FinalBlock():
    try:
        f = open("source.txt",'r')
        content = f.read()
        print(content)
    except FileNotFoundError:
        print("File not Found..!!")
    finally:
        print("This Block will Executes!!")

#Generic Exception
def G_exception():
    try:
        a = int("abc")

    except Exception as error:
        print("Content is String ", error)

#Nested Exception
def Nested_Exception():
    try:
        num = int(input("Enter a number : "))
        try:
            c = 10 / 0
        except ZeroDivisionError:
            print("Can't Divide by Zero")
    except ValueError:
        print("Value Error!!")

#User-defined Exception
def Balance():
    try:
        balance = int(input("Enter Balance : "))
        if balance < 0:
            raise ValueError("\nBalance cannot be less than zero")
        print("Balance : ", balance)
    except ValueError as e:
        print("Error.. !!", e)

def main():
    while True:
        print("\n1. ZeroDivisionError")
        print("2. ValueError")
        print("3. TryExceptElse")
        print("4. Final Block")
        print("5. Generic Exception")
        print("6. Nested Exception")
        print("7. User-defined Exception")
        print("8. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            ZeroDivision()
        elif choice == "2":
            valueError()
        elif choice == "3":
            TryExceptElse()
        elif choice == "4":
            FinalBlock()
        elif choice == "5":
            G_exception()
        elif choice == "6":
            Nested_Exception()
        elif choice == "7":
            Balance()
        elif choice == "8":
            break
        

if __name__ == "__main__":
    main()





