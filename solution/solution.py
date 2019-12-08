

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
    return [8*inputs[0], 16*inputs[0]]


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


def _more_else_if(inputs=None):
    val = inputs[0]
    if val >= 80:
        return ['A']
    elif val >= 65:
        return ['B']
    elif val >= 45:
        return ['C']
    elif val >= 25:
        return ['D']
    return ['F']


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


def _complex_if(inputs=None):
    return max(inputs)


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


def _fibonacci(inputs=None):
    outputs = [0, 1]
    value = inputs[0]
    if value == 0:
        return [0]
    elif value == 1:
        return outputs

    a = 0
    b = 1
    c = 0
    while c < value:
        c = a + b
        if c < value:
            outputs.append(c)
        a = b
        b = c
    return outputs


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
        elif (i % 3 == 0):
            lst.append('Fizz')
        elif (i % 5 == 0):
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst


# Compare two lists
def _list_compare(inputs=None):
    list0_sum = sum(inputs[0])
    list1_sum = sum(inputs[1])
    lst = []
    if list0_sum > list1_sum:
        msg = 'sumList1[' + str(list0_sum) + '] > sumList2[' + str(list1_sum) + ']'
        lst.append(msg)
    else: 
        msg = 'sumList1[' + str(list0_sum) + '] < sumList2[' + str(list1_sum) + ']'
        lst.append(msg)
    return lst


# MinMax of lists
def _list_minmax(inputs=None):
    maxVal = max(inputs[0])
    minVal = min(inputs[0])
    msg = 'max=' + str(maxVal) + ',min=' + str(minVal)
    return [msg]


# Make the sublist of a list
def _list_sublist(inputs=None):
    print('list-sublist')
    oldList = inputs[0]
    average = sum(oldList) / len(oldList)
    print('average=',average)
    newList = []
    for i in range(len(oldList)):
        if (oldList[i] > average) : 
            newList.append(oldList[i])
    print('newList',newList)
    return [newList]


SOLUTIONS = {
    'intro': _intro,
    'basic_arithmetic': _basic_arithmetic,
    'input_and_variables': _reverse_with_vars,
    'input_variables_arithmetic': _basic_velocity,
    'multiply_by_eight': _multiply_by_eight,
    'basic_if': _basic_if,
    'else': _if_else,
    'else_if' : _if_else_if_else,
    'more_else_if': _more_else_if,
    'and_or': _and_or,
    'complex_if': _complex_if,
    'for_loops_0': _for_loops_0,
    'for_if': _for_if,
    'while_loop': _while_loop,
    'while_decimal': _while_decimal,
    'fibonacci': _fibonacci,
    'fizz_buzz': _fizz_buzz,
    'list_basic' : _list_basic,
    'list_index' : _list_index,
    'list_sort' : _list_sort,
    'list_compare' : _list_compare,
    'list_minmax' : _list_minmax,
    'list_sublist' : _list_sublist,

}
