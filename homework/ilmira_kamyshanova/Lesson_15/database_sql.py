import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

insert_student_query = "INSERT INTO students (name, second_name) VALUES(%s, %s)"
insert_book_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
insert_group_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES(%s, %s, %s)"
insert_subject_query = "INSERT INTO subjets (title) VALUES (%s)"
insert_lesson_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
insert_mark_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"

select_students_join_marks_query = '''
SELECT s.name, s.second_name, m.value
FROM students s
JOIN marks m ON s.id = m.student_id
WHERE s.id = %s
'''
select_students_join_books_query = '''
SELECT s.name, s.second_name, b.title
FROM students s
JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = %s
'''
select_join_all_query = '''
SELECT s.name, s.second_name, g.title AS `group`, b.title AS book,
m.value AS mark, l.title AS lesson, sub.title AS subject
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sub ON sub.id = l.subject_id
WHERE s.id = %s
'''

cursor = db.cursor(dictionary=True)
cursor.execute(insert_student_query, ('Mary', 'Markov'))
student_id = cursor.lastrowid

cursor.executemany(
    insert_book_query, [
        ('Tudors', student_id),
        ('Pushkin', student_id),
        ('Lermontov', student_id)
    ]
)

cursor.execute(insert_group_query, ('History', 'may 14', 'feb 14'))
group_id = cursor.lastrowid

cursor.execute('UPDATE students SET group_id  = %s WHERE id = %s', (group_id, student_id))

cursor.execute(insert_subject_query, ['Geology subject'])
subject_geo_id = cursor.lastrowid

cursor.execute(insert_subject_query, ['High math subject'])
subject_math_id = cursor.lastrowid

cursor.execute(insert_lesson_query, ('Lesson 1 for Geology subject', subject_geo_id))
lesson_geo1_id = cursor.lastrowid

cursor.execute(insert_lesson_query, ('Lesson 2 for Geology subject', subject_geo_id))
lesson_geo2_id = cursor.lastrowid

cursor.execute(insert_lesson_query, ('Lesson 1 for High math subject', subject_math_id))
lesson_math1_id = cursor.lastrowid

cursor.execute(insert_lesson_query, ('Lesson 2 for High math subject', subject_math_id))
lesson_math2_id = cursor.lastrowid

cursor.executemany(
    insert_mark_query, [
        (5, lesson_geo1_id, student_id),
        (4, lesson_geo2_id, student_id),
        (3, lesson_math1_id, student_id),
        (2, lesson_math2_id, student_id)
    ]
)

print('Student and marks: ')
cursor.execute(select_students_join_marks_query, [student_id])
print(cursor.fetchall())

print('Student and books: ')
cursor.execute(select_students_join_books_query, [student_id])
print(cursor.fetchall())

print('All info about student: ')
cursor.execute(select_join_all_query, [student_id])
print(cursor.fetchall())

db.commit()
db.close()
