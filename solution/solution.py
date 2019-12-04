

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
    a = inputs[0]
    b = inputs[1]
    c = inputs[2]
    d = inputs[3]
    lst = []
    if(a > b and c > d):
        lst.append('Both are true')
    else:
        lst.append('Both are NOT true')
    if(a > b or c > d):
        lst.append('One is true')
    else:
        lst.append('Neither is true')
    return lst

# print numbers from 0 to the integer
def _for_loops_0(inputs=None):
    a = inputs[0]
    lst = []
    for i in range(a+1):
        lst.append(i)
    return lst

# print only even numbers from 0 to the integer
def _for_if(inputs=None):
    a = inputs[0]
    lst = []
    for i in range(a+1):
        if (i % 2 == 0):
            lst.append(i)
    return lst

# print a sum of integers from 0 to up until the integer
def _while_loop(inputs=None):
    a = inputs[0]
    lst = []
    sum = 0
    for i in range(a+1):
        sum += i
    lst.append(sum)
    return lst

# print converted binary values (from decimal) sequentially
def _while_decimal(inputs=None):
    decimal = inputs[0]
    lst = []
    while decimal > 0:
        lst.append(decimal % 2)
        decimal = round(decimal // 2)
    return lst

# print true / false based on validation if the number is prime
def _while_prime(inputs=None):
    num = inputs[0]
    lst = []
    prime = True
    for i in range(2, num):
        # print('(debug)',num, ' % ', i, ' == ',(num % i))
        if(num % i) ==0:
            prime = False
            break
    lst.append(prime)
    return lst

# print sum of integers inside a list
def _list_basic(inputs=None):
    a = inputs[0]
    sum = 0
    for i in range(len(a)):
        # print('(debug)', i, ':',a[i])
        sum += a[i]
    lst = [sum]
    return lst

# print the index of the maximum integer
def _list_index(inputs=None):
    a = inputs[0]
    max = -1
    maxInd = 0
    for i in range(len(a)):
        if (a[i] > max) : 
            max = a[i]
            maxInd = i
    lst = [maxInd]
    return lst

# print only even numbers sorted in ascending order
def _list_sort(inputs=None):
    a = inputs[0]
    a.sort()
    lst = []
    for i in range(len(a)):
        if (a[i] % 2 == 0) : 
            lst.append(a[i])
    return lst

# FizzBuzz game
def _fizz_buzz(inputs=None):
    fizzbuzz = inputs[0]
    lst = []
    for i in range(1, fizzbuzz+1):
        if (i % 15 == 0):
            lst.append('FizzBuzz')
        elif (i % 3 ==0):
            lst.append('Fizz')
        elif (i % 5 ==0):
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst

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
    'for_loops_0' : _for_loops_0,
    'for_if' : _for_if,
    'while_loop' : _while_loop,
    'while_decimal' : _while_decimal,
    'while_prime' : _while_prime,
    'list_basic' : _list_basic,
    'list_index' : _list_index,
    'list_sort' : _list_sort,
    'fizz_buzz' : _fizz_buzz,

}
