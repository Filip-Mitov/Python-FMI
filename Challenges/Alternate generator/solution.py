import itertools

a = lambda: itertools.count(1, 1)
b = lambda: itertools.count(-1, -1)

def alternate(*arguments):
    all_arguments = [one_function() for one_function in arguments]
    while True:
        for index in range(len(arguments)):
            yield next(all_arguments[index])
