def repeat_me(func):

    def wrapper(*args, count):
        for i in range(count):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me_2(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper
    return decorator


@repeat_me_2(count=2)
def example_2(text):
    print(text)


example_2('print me')
