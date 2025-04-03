secret_number = 7

while True:
    user_gess_number = int(input('Угадайте загаданную цифру: '))
    if secret_number != user_gess_number:
        print('попробуйте снова')
        continue
    print('Поздравляю! Вы угадали!')
    break
