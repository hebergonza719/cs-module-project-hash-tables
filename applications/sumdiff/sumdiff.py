"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
q_list = list(q)

def f(x):
    return x * 4 + 6

# Your code here
def print_lines(a, func_A, b, func_B, c, func_C, d, func_D):
    lines = {}
    lines[f'f({a}) + f({b}) = f({c}) - f({d})'] = f'{func_A} + {func_B} = {func_C} - {func_D} 1'
    lines[f'f({b}) + f({a}) = f({c}) - f({d})'] = f'{func_B} + {func_A} = {func_C} - {func_D} 2' #1
    lines[f'f({d}) + f({b}) = f({c}) - f({a})'] = f'{func_A} + {func_B} = {func_C} - {func_A} 3'
    lines[f'f({a}) + f({d}) = f({c}) - f({b})'] = f'{func_A} + {func_D} = {func_C} - {func_B} 4'
    lines[f'f({b}) + f({d}) = f({c}) - f({a})'] = f'{func_B} + {func_D} = {func_C} - {func_A} 5' #3
    lines[f'f({d}) + f({a}) = f({c}) - f({b})'] = f'{func_D} + {func_A} = {func_C} - {func_B} 6' #2
    for (k, v) in lines.items():
        print(k + "   " + v)


func_C_lookup = {}

for x in q_list:
    func_C_lookup[f(x)] = x #{10: 1, 18: 3, 22: 4, 34: 7, 54: 12}

for (idx_A, a) in enumerate(q_list):
    func_A = f(a)
    for (idx_B, b) in enumerate(q_list[idx_A:]):
        func_B = f(b)
        for (idx_D, d) in enumerate(q_list[(idx_A + idx_B):]):
            func_D = f(d)
            func_C = func_A + func_B + func_D
            if func_C in func_C_lookup:
                print_lines(a, func_A, b, func_B, func_C_lookup[func_C], func_C, d, func_D)