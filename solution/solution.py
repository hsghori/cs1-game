

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


SOLUTIONS = {
    'intro': _intro,
    'basic_arithmetic': _basic_arithmetic,
    'input_and_variables': _reverse_with_vars,
    'input_variables_arithmetic': _basic_velocity,
    'multiply_by_eight': _multiply_by_eight,
}
