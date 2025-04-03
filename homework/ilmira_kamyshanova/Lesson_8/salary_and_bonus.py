import random

salary = int(input('Enter the salary, please: '))
bonus = random.choice([True, False])

new_salary = salary
if bonus:
    new_salary += random.randint(1, 10000)
print(f'{salary}, {bonus} - ${new_salary}')
