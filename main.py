def evaluate_expression(expression):
    """Вычисляет значение арифметического выражения, заданного строкой."""
    stack = []
    current_number = 0
    operation = '+'
    for i in range(len(expression)):
        if expression[i].isdigit():
            current_number = current_number * 10 + int(expression[i])
        if not expression[i].isdigit() or i == len(expression) - 1:
            if operation == '+':
                stack.append(current_number)
            elif operation == '-':
                stack.append(-current_number)
            current_number = 0
            operation = expression[i]
    return sum(stack)

def generate_expressions(numbers, target_sum, current_expression="", current_value=0):
    """Генерирует все возможные арифметические выражения, которые можно получить из заданных чисел, и проверяет их на равенство целевой сумме."""
    if not numbers:
        if current_value == target_sum:
            print(current_expression)
            return True
        return False
    found_solution = False
    for i in range(1, len(numbers) + 1):
        current_number = int("".join(numbers[:i]))
        remaining_numbers = numbers[i:]
        if current_expression:
            found_solution |= generate_expressions(remaining_numbers, target_sum, current_expression + "+" + str(current_number), current_value + current_number)
            found_solution |= generate_expressions(remaining_numbers, target_sum, current_expression + "-" + str(current_number), current_value - current_number)
        else:
            found_solution |= generate_expressions(remaining_numbers, target_sum, str(current_number), current_number)
    return found_solution

numbers = [str(i) for i in range(9, -1, -1)]

target_sum = 200

if not generate_expressions(numbers, target_sum):
    print("No solution found.")
