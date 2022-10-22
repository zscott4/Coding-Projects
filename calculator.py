import sys
def add(x,y):
    return round(x + y,1)
def sub(x,y):
    return round(x - y,1)
def multi(x,y):
    return round(x * y,1)
def div(x,y):
    return round(x / y,1)

def calculator():
    while True:
        print("""Let's calculate!
        1) Add
        2) Subtract
        3) Mutliply
        4) Divide
        5) Exit""")
        ask = input('Please select one of the options above:')
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if ask == '1':
            print(add(num1, num2))
        elif ask == '2':
            print(sub(num1, num2))
        elif ask == '3':
            print(multi(num1, num2))
        elif ask == '4':
            print(div(num1, num2))
        elif ask == '5':
            print("Have a nice day!")
            sys.exit

def main():
    calculator()
main()