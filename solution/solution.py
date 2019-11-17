

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


# return all integers which are only positive
def _basic_if(inputs=None):
    lst = []
    if(inputs[0] > 0):
        lst.append(inputs[0])
    if(inputs[1] > 0): 
        lst.append(inputs[1])
    if(inputs[2] > 0): 
        lst.append(inputs[2])
    return lst


# return absolute integer
def _if_else(inputs=None):
    if(inputs[0] > 0):
        return [inputs[0]]
    else:
        return [-1*inputs[0]]


# return value according to the requirement
def _if_else_if_else(inputs=None):
    a = inputs[0]
    b = inputs[1]
    c = inputs[2]
    d = inputs[3]
    if(a > b):
        return [a + b]
    elif( c < d):
        return [c + d]
    else: 
        return ['No Answer']

def _and_or(inputs=None):
    return []

SOLUTIONS = {
    'intro': _intro,
    'basic_arithmetic': _basic_arithmetic,
    'input_and_variables': _reverse_with_vars,
    'input_variables_arithmetic': _basic_velocity,
    'multiply_by_eight': _multiply_by_eight,
    'basic_if' : _basic_if,
    'else' : _if_else,
    'if_else_if_else' : _if_else_if_else,
    'and_or' : _and_or,
}
