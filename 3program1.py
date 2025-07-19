# 1. Simple CalculatorWrite a Python program that:
#Takes two numbers and an operator (+, -, *, /) from the user.
#Performs the operation and displays the result.

print("Hello, welcome here ")
Number1 = float(input("enter the first number: "))
Number2 = float(input("enter the seconfd element: ") )
operation = input("Enter the operation you need to performe (+,-,*,/): ")

if operation == "+":

    add = Number1+Number2
    print("Addition of two no.",  add)
elif operation == "*":

    multi = Number1* Number2
    print("Multiplication of Two no.",multi)
elif operation == "-":

    sub= Number1- Number2
    print("Subtration of two no.",sub)
elif operation == "/":
    div = Number1/Number2
    print("division opf Two no.",div)


