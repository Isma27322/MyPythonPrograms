def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            return "Cannot divide by zero"
    return result

def get_operator_choice(j):
    print("Select operator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operator_choice = input("Enter operator #"+(str)i+1+" choice (1/2/3/4): ")
    return operator_choice

num_count = int(input("Enter the number of values: "))
numbers = []
for i in range(num_count):
    num = float(input(f"Enter value {i+1}: "))
    numbers.append(num)

operator_count = int(input("Enter the number of operators: "))
operators = []
for i in range(operator_count):
    operator = get_operator_choice(i)
    operators.append(operator)

result = numbers[0]
for i in range(len(operators)):
    if operators[i] == '1':
        result = add([result, numbers[i + 1]])
    elif operators[i] == '2':
        result = subtract([result, numbers[i + 1]])
    elif operators[i] == '3':
        result = multiply([result, numbers[i + 1]])
    elif operators[i] == '4':
        result = divide([result, numbers[i + 1]])

print("Result:", result)
