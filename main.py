print()

number1 = float(input("Enter the first number: "))
operator = input("Enter the operator [+ - * /]: ")
number2 = float(input("Enter the second number: "))

if operator == "+":
  result = number1 + number2
elif operator == "-":
  result = number1 - number2
elif operator == "*":
  result = number1 * number2
elif operator == "/":
  result = number1 / number2

print(f"\nThe result is {result}.")
