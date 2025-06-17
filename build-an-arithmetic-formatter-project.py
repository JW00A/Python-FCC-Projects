#** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    a_list_of_digits = []
    a_list_of_operators = []

    counter = 0

    for problem in problems:
        for char in problem:
            if (char == '-' or char == '+'):
                a_list_of_operators.append(char)
            else:
                a_list_of_digits.append(char)
            
            if char.isalpha():
                counter += 1
        a_list_of_digits.append('-')

    if len(a_list_of_operators) != len(problems):
        return "Error: Operator must be '+' or '-'."
    
    if counter > 0:
        return "Error: Numbers must only contain digits."

    digit_counter = 0
    for digit in a_list_of_digits:
        if digit == ' ' or digit == '-':
            if digit_counter > 4:
                return "Error: Numbers cannot be more than four digits."
            digit_counter = 0
        else:
            digit_counter += 1

    index_of_char = 0

    first_str = ''
    second_str = ''
    third_str = ''

    current_char = ''
    dashes = ''

    for problem in problems:
        if '+' in problem:
            index_of_char = problem.index('+')
            current_char = '+'
        if '-' in problem:
            index_of_char = problem.index('-')
            current_char = '-'

        first_operand = problem[:index_of_char].strip(' ')
        second_operand = problem[index_of_char+1:].strip(' ')
        first_operand_len = len(first_operand)
        second_operand_len = len(second_operand)

        max_operand_num = max(first_operand_len, second_operand_len)
    
        first_str += first_operand.rjust(max_operand_num + 2) + ' ' * 4
        second_str += current_char + ' ' + second_operand.rjust(max_operand_num) + ' ' * 4

        dashes = dashes + '-' * (max_operand_num + 2) + ' ' * 4
        
        third_operand = ''
        first_operand_int = int(first_operand)
        second_operand_int = int(second_operand)

        if show_answers == True:
            if current_char == '+':
                third_operand = str(first_operand_int + second_operand_int)
            else:
                if first_operand_int > second_operand_int:
                    third_operand = str(first_operand_int - second_operand_int)
                else:
                    third_operand = '-' + str(second_operand_int - first_operand_int)
        
        third_str += third_operand.rjust(max_operand_num + 2) + ' ' * 4

    if not show_answers:
        output = first_str.rstrip() + '\n' + second_str.rstrip() + '\n' + dashes.rstrip()
    else:
        output = first_str.rstrip() + '\n' + second_str.rstrip() + '\n' + dashes.rstrip() + '\n' + third_str.rstrip()

    return output

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')

#** end of main.py **
