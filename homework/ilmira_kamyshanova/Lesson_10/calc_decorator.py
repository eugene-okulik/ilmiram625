first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))


def calc_decorator(func):

    def wrapper(first, second):
        if second < 0 or first < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            operation = '+'
        return func(first, second, operation)

    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            print('Error! Can`t divide to zero!')
    else:
        print('There is no math operation. Try again, please!')


print(f'Result is: {calc(first_number, second_number)}')
