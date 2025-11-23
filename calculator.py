# calculator.py
# Simple Calculator Program
# Coder is RAMAN RAJ SHRIVASTAVA
# ROLL NO.:- 2501010021
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator.")
            continue

        print(f"Result: {result}")

        repeat = input("Do you want to calculate again? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting calculator...")
            break

if __name__ == "__main__":
    main()
