import sys


def fibo_numbers():
    prev_number, next_number = 0, 1
    while True:
        yield prev_number
        prev_number, next_number = next_number, prev_number + next_number


sys.set_int_max_str_digits(100000)
count = 0
for number in fibo_numbers():
    if count == 5 or count == 200 or count == 1000 or count == 100000:
        print(number)
        if count == 100000:
            break
        count += 1
        continue
    count += 1
