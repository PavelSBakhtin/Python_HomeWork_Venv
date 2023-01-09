# простой калькулятор, созданный в виртуальном окружении

numA = int(input("Enter number A: "))
sing = input("Enter operation sing: ")
numB = int(input("Enter number B: "))

def calc(a, s, b):
    result = 0
    if s == "+":
        result = a + b
    if s == "-":
        result = a - b
    if s == "*":
        result = a * b
    if s == "/":
        result = a / b
    if s == "^":
        result = a ** b
    return result

result = calc(numA, sing, numB)
print(f"{numA} {sing} {numB} = {result}")
