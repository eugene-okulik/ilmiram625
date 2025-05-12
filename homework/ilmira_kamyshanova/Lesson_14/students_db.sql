INSERT INTO students (name, second_name) VALUES('Masha', 'Petrova')

INSERT INTO books (title, taken_by_student_id) VALUES
('Math', 20298), 
('Biology', 20298), 
('Idiot', 20298)

INSERT INTO `groups` (title, start_date, end_date) VALUES('Natural science', 'may 9', 'feb 9')

UPDATE students SET group_id  = 5029
WHERE id = 20298

INSERT INTO subjets (title) VALUES ('Geology subject'), ('High math subject'), ('Bio subject')

INSERT INTO lessons (title, subject_id) VALUES
('Lesson 1 for Geology subject', 10263),
('Lesson 2 for Geology subject', 10263),
('Lesson 1 for High math subject', 10264),
('Lesson 2 for High math subject', 10264),
('Lesson 1 for Bio subject', 10265),
('Lesson 2 for Bio subject', 10265)

INSERT INTO marks (value, lesson_id, student_id) VALUES
(5, 9731, 20298),
(4, 9732, 20298),
(5, 9733, 20298),
(5, 9734, 20298),
(5, 9735, 20298),
(5, 9736, 20298)

SELECT s.name, s.second_name, m.value FROM students s JOIN marks m ON s.id = m.student_id WHERE s.id = 20298

SELECT s.name, s.second_name, b.title FROM students s JOIN books b ON s.id = b.taken_by_student_id WHERE s.id = 20298

SELECT s.name, s.second_name, g.title AS `group`, b.title AS book, m.value AS mark, l.title AS lesson, sub.title AS subject FROM students s 
JOIN `groups` g ON s.group_id = g.id 
JOIN books b ON s.id = b.taken_by_student_id 
JOIN marks m ON s.id = m.student_id 
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjets sub ON sub.id = l.subject_id 
WHERE s.id = 20298


