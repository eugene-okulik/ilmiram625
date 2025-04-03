text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'


def print_result(text: str):
    number = int(text.split()[-1])
    print(f'Summ result for {number}: {number + 10}')


print_result(text_1)
print_result(text_2)
print_result(text_3)
