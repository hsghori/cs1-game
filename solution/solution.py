

def _intro(inputs=None):
    return ['Hello world!']


def _basic_arithmetic(inputs=None):
    return [3, 24, 1]

def _basic_if(inputs=None):
    return [True]

SOLUTIONS = {
    'intro': _intro,
    'basic_arithmetic': _basic_arithmetic,
    'basic_if': _basic_if,
}
