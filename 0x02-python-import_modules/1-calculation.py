#!/usr/bin/python3
def main():
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    print(f"add(a, b) = {add(a, b)}")
    print(f"subtract(a, b) = {subtract(a, b)}")
    print(f"multiply(a, b) = {multiply(a, b)}")
    print(f"divide(a, b) = {divide(a, b)}")
if __name__ == "__main__":
    main()
