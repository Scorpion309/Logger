import main

@main.decorator
def function_from_task(*args, **kwargs):
    result = 0
    for key in kwargs.keys():
        result += kwargs[key]
    return result

function_from_task('arg4', 'arg5', 'arg6', a = 4, b = 5, c = 6)
