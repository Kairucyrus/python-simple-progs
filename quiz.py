import random
import numpy as np

"""in this program, we use random module to randomly generate numbers in the range
defined (min_operand, max_opernd). Two integers, max_operand and min_operand are the operands 
we use to perform random operations on them; operators are also selected at random
from a list, using random.choice()
an expression (expr), is taken as a concatenation of left, operator and right operands
and for every expression, an answer is calculated using the python eval(); instead of the need to 
have several if statements for all the four operators.

"""
operators = ["+", "/", "-", "*"]
min_operand = 5
max_operand = np.power(10, min_operand)

def generate_quiz():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answwer = eval(expr)
    return expr, answwer


expr, answer = generate_quiz()
print(expr, "=", answer)

    