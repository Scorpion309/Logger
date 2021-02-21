def decorator(function_to_decorate):

    def log_calls(*args, format='JSON', **kwargs):
        import datetime
        result = function_to_decorate(*args, **kwargs)
        callable = function_to_decorate.__name__
        if format == 'JSON':
            import json
            data = {'timestamp': datetime.datetime.now().isoformat(),
                    'callable': callable,
                    'args': args,
                    'kwargs': kwargs,
                    'result': result}
            with open('app.log', 'a') as log:
                log.write('JSON: \n')
                json.dump(data, log, indent=4)
                log.write('\n')

        elif format == 'YAML':
            import yaml
            data = [{'timestamp': [datetime.datetime.now().isoformat()]},
                    {'callable': callable},
                    {'args': args},
                    {'kwargs': kwargs},
                    {'result': result}]
            with open('app.log', 'a') as log:
                log.write('YAML: \n')
                yaml.dump(data, log)
                log.write('\n')

        else:
            print('Введенный формат не поддерживается')
    return log_calls

if __name__ == '__main__':
    @decorator
    def test(*args, **kwargs):
        return "GOOD JOB"

    test('arg1', 'arg2', 'arg3', format = 'YAML', a = 1, b = 2, c = 3)



