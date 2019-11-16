

def _intro(inputs=None):
    return ['Hello world!']


def _basic_arithmetic(inputs=None):
    return [sum(inputs)]


def _reverse_with_vars(inputs=None):
    return inputs[::-1]


def _basic_velocity(inputs=None):
    time = inputs[0]
    velocity = inputs[1]
    acceleration = inputs[2]
    return [velocity * time + 0.5 * acceleration * time ** 2]


def _multiply_by_eight(inputs=None):
    # note that for this problem, the students are only provided with addition blocks
    # so in the best case their solution will look like:
    #
    #     x = input
    #     x = x + x  # x = input * 2^1
    #     x = x + x  # x = input * 2^2
    #     x = x + x  # x = input * 2^3 = input * 8
    return [8*i for i in inputs]

def _basic_if(inputs=None):
    return [sum(inputs)]

def _if_else(inputs=None):
    return [inputs[0] - inputs[1]]

def _if_else_if_else(inputs=None):
    a = inputs[0]
    b = inputs[1]
    c = inputs[2]
    d = inputs[3]
    print(a,b,c,d)
    ret = 0
    if(a > b):
        ret = a + b
    elif( c < d):
        ret = c + d
    else: 
        ret = 'No Answer' 
    return [ret]


SOLUTIONS = {
    'intro': _intro,
    'basic_arithmetic': _basic_arithmetic,
    'input_and_variables': _reverse_with_vars,
    'input_variables_arithmetic': _basic_velocity,
    'multiply_by_eight': _multiply_by_eight,
    'basic_if' : _basic_if,
    'else' : _if_else,
    'if_else_if_else' : _if_else_if_else,
}