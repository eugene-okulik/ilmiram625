import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

select_query = '''
SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title,
sub.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sub ON sub.id = l.subject_id
'''

cursor = db.cursor(dictionary=True)
cursor.execute(select_query)

data_from_db = cursor.fetchall()
db.close()

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


def read_file():
    with open(data_file_path, newline='') as csv_file:
        for row in csv.DictReader(csv_file):
            yield row


for line in read_file():
    if line not in data_from_db:
        print(f'Line is not from database: \n{line}')
