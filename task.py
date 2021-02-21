import main

@main.decorator
def test_function(*args, **kwargs):
    result = 0
    for key in kwargs.keys():
        result += kwargs[key]
    return result

test_function('arg4', 'arg5', 'arg6', a = 4, b = 5, c = 6)
