import re


def add_spaces(num):
    """
    Helper function to return a string of a number of spaces.
    
    Parameters
    ----------
    num : int
        The number of spaces to return.

    Returns
    -------
    string
        A string of a number of spaces.
    """
    return num * " "

    
def add_dashes(num):
    """
    Helper function to return a string of a number of hyphens.
    
    Parameters
    ----------
    num : int
        The number of hyphens/dashes to return.

    Returns
    -------
    string
        A string of a number of hyphens.
    """
    return "-" * num


def is_greater_than_4_digits(num):
    """
    Helper function to determine if a number is greater than 4 digits.
    
    Parameters
    ----------
    num : int
        The number to check.

    Returns
    -------
    bool
        Returns true if the number is greater than 4 digits. 
    """
    return abs(num) / 10000 >= 1



def create_problem_dict(problem):
    problem_components = problem.split()

    data = {
        "first_operand": problem_components[0],
        "second_operand": problem_components[2],
        "operation": problem_components[1],
    }

    most_digits = len(data["first_operand"]) if len(
        data["first_operand"]) > len(data["second_operand"]) else len(
            data["second_operand"])
    data["format_width"] = most_digits + 2

    return data



def check_for_errors(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        problem_components = problem.split()

        if (problem_components[1] != "+" and problem_components[1] != "-"):
            return "Error: Operator must be '+' or '-'."

        contains_char = "[A-Za-z]"
        operand_first = problem_components[0]
        operand_second = problem_components[2]
        if (re.search(contains_char, operand_first)
                or re.search(contains_char, operand_second)):
            return "Error: Numbers must only contain digits."

        try:
            operand_first = int(operand_first)
            operand_second = int(operand_second)

            if (is_greater_than_4_digits(operand_first)
                    or is_greater_than_4_digits(operand_second)):
                return "Error: Numbers cannot be more than four digits."
        except:
            return "Error: Number format could not be parsed as an integer."




def calc_solution(first_operand, second_operand, operation):
    first_operand = int(first_operand)
    second_operand = int(second_operand)

    result = None
    if (operation == "+"):
        result = first_operand + second_operand
    elif (operation == "-"):
        result = first_operand - second_operand

    return result


def formatter(problem_dict):
    formatted_problem = []

    line_1 = f'{add_spaces(problem_dict["format_width"] - len(problem_dict["first_operand"]))}{problem_dict["first_operand"]}'
    line_2 = f'{problem_dict["operation"]}{add_spaces(problem_dict["format_width"] - 1 - len(problem_dict["second_operand"]))}{problem_dict["second_operand"]}'
    line_3 = add_dashes(problem_dict["format_width"])

    result = calc_solution(problem_dict["first_operand"], problem_dict["second_operand"], problem_dict["operation"])

    line_4 = f'{add_spaces(problem_dict["format_width"] - len(str(result)))}{result}'
    
    formatted_problem.append(line_1)
    formatted_problem.append(line_2)
    formatted_problem.append(line_3)
    formatted_problem.append(line_4)
    return formatted_problem


def format_with_new_line(show_answer, arranged_problem_lines):
    formatted_in_one_string = ""
    if show_answer:
        formatted_in_one_string = "\n".join(arranged_problem_lines)
    else:
        formatted_in_one_string = "\n".join(arranged_problem_lines[:3])
    return formatted_in_one_string



def arithmetic_arranger(problems, show_answer=False):
    
    error_flagged = check_for_errors(problems)
    if (error_flagged):
        return error_flagged

    problem_set = []

    for problem in problems:
        problem_data = create_problem_dict(problem)
        formatted_problem = formatter(problem_data)
        problem_set.append(formatted_problem)

    print(problem_set)
    problem_set_by_line = []

    
    for line in range(4):
        components_of_line = []
        for problem in problem_set:
            components_of_line.append(problem[line])
        problem_set_by_line.append(components_of_line)
            

    
    arranged_problems = []

    print(problem_set_by_line)
    for line in problem_set_by_line:
        formatted_line = "    ".join(line)
        arranged_problems.append(formatted_line)


    return format_with_new_line(show_answer, arranged_problems)
