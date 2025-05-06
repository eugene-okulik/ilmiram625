import os
import datetime

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

def read_file():
    with open(data_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line

date_list = []

for data_line in read_file():
    date = datetime.datetime.strptime(data_line.split(' - ')[0][3:], '%Y-%m-%d %H:%M:%S.%f')
    date_list.append(date)

print(f'{date_list[0]} after one week is: {date_list[0] + datetime.timedelta(weeks=1)}')
print(f'{date_list[1]} was {date_list[1].strftime("%A")}')
print(f'{date_list[2]} was {(datetime.datetime.now() - date_list[2]).days} days ago')
