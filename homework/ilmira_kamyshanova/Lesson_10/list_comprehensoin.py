PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split()

new_dict = {price_list[i]: int(price_list[i + 1][:-1]) for i in range(len(price_list) - 1) if i % 2 == 0}
print(new_dict)
