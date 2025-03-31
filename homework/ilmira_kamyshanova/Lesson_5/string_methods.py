text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

index_of_number_1 = text_1.index(':') + 2
index_of_number_2 = text_2.index(':') + 2
index_of_number_3 = text_3.index(':') + 2

number_1 = int(text_1[index_of_number_1:])
number_2 = int(text_2[index_of_number_2:])
number_3 = int(text_3[index_of_number_3:])

print(f'Summ result for number one: {number_1 + 10}')
print(f'Summ result for number two: {number_2 + 10}')
print(f'Summ result for number three: {number_3 + 10}')
