INSERT INTO students (name, second_name) VALUES('Masha', 'Petrova')

INSERT INTO books (title, taken_by_student_id) VALUES
('Math', (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')), 
('Biology', (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')), 
('Idiot', (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova'))

INSERT INTO `groups` (title, start_date, end_date) VALUES('Natural science', 'may 9', 'feb 9')

UPDATE students SET group_id  = (SELECT id FROM `groups` WHERE title = 'Natural science' and start_date = 'may 9' and end_date = 'feb 9')
WHERE name = 'Masha' and second_name = 'Petrova'

INSERT INTO subjets (title) VALUES ('Geology subject'), ('High math subject'), ('Bio subject')

INSERT INTO lessons (title, subject_id) VALUES
('Lesson 1 for Geology subject', (SELECT id FROM subjets WHERE title = 'Geology subject')),
('Lesson 2 for Geology subject', (SELECT id FROM subjets WHERE title = 'Geology subject')),
('Lesson 1 for High math subject', (SELECT id FROM subjets WHERE title = 'High math subject')),
('Lesson 2 for High math subject', (SELECT id FROM subjets WHERE title = 'High math subject')),
('Lesson 1 for Bio subject', (SELECT id FROM subjets WHERE title = 'Bio subject')),
('Lesson 2 for Bio subject', (SELECT id FROM subjets WHERE title = 'Bio subject'))

INSERT INTO marks (value, lesson_id, student_id) VALUES
(5, (SELECT id FROM lessons WHERE title = 'Lesson 1 for Geology subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')),
(4, (SELECT id FROM lessons WHERE title = 'Lesson 2 for Geology subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')),
(5, (SELECT id FROM lessons WHERE title = 'Lesson 1 for High math subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')),
(5, (SELECT id FROM lessons WHERE title = 'Lesson 2 for High math subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')),
(5, (SELECT id FROM lessons WHERE title = 'Lesson 1 for Bio subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova')),
(5, (SELECT id FROM lessons WHERE title = 'Lesson 2 for Bio subject'), (SELECT id FROM students WHERE name = 'Masha' and second_name = 'Petrova'))

SELECT s.name, s.second_name, m.value FROM students s JOIN marks m ON s.id = m.student_id WHERE name = 'Masha' and second_name = 'Petrova' 

SELECT s.name, s.second_name, b.title FROM students s JOIN books b ON s.id = b.taken_by_student_id WHERE name = 'Masha' and second_name = 'Petrova' 

SELECT s.name, s.second_name, g.title AS `group`, b.title AS book, m.value AS mark, l.title AS lesson, sub.title AS subject FROM students s 
JOIN `groups` g ON s.group_id = g.id 
JOIN books b ON s.id = b.taken_by_student_id 
JOIN marks m ON s.id = m.student_id 
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjets sub ON sub.id = l.subject_id 
WHERE name = 'Masha' and second_name = 'Petrova' 


