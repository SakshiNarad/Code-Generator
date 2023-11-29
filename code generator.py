import random

def generate_code():
  
    variables = ['a', 'b', 'c', 'x', 'y', 'z']

  
    operations = ['+', '-', '*', '/']

    
    variable1 = random.choice(variables)
    variable2 = random.choice(variables)
    operation = random.choice(operations)

  
    code = f'def calculate({variable1}, {variable2}):'
    code += f'\n    result = {variable1} {operation} {variable2}'
    code += '\n    return result'

    return code


print(generate_code())
