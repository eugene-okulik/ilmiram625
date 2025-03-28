my_dict = {'tuple': (1, 'two', 3, 4, 5), 'list': [1, 2, 'tree', 3, 4, 5],
           'dict': {1: 1, 2: 2, 3: 3, 'four': 'four', 5: 5}, 'set': {1, 2, 3, 4, 'five'}}
print(f'Last element in tuple is: {my_dict["tuple"][-1]}')

my_dict['list'].append('last_element')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 6
my_dict['dict'].pop(3)

my_dict['set'].add(6)
my_dict['set'].pop()

print(f'Dictionary: {my_dict}')
