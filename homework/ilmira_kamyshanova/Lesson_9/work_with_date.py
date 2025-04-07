import datetime

date_str = 'Jan 15, 2023 - 12:05:33'

date_python = datetime.datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')

print(date_python.strftime('%B'))
print(date_python.strftime('%d.%m.%Y, %H:%M'))
