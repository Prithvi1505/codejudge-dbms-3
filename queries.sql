-- IN and BETWEEN
SELECT student_name FROM Students WHERE department IN ('CS', 'Math') 
AND enrollment_year BETWEEN 2023 AND 2025;

-- IS NOT NULL
SELECT * FROM Courses WHERE instructor_name IS NOT NULL;

-- GROUP BY + HAVING
SELECT department, AVG(marks_obtained) as avg_marks
FROM Enrollments e JOIN Students s ON e.student_id = s.student_id
GROUP BY department HAVING AVG(marks_obtained) > 70;

-- Joins
SELECT * FROM Students s INNER JOIN Enrollments e ON s.student_id = e.student_id;
SELECT * FROM Students s LEFT JOIN Enrollments e ON s.student_id = e.student_id;
SELECT * FROM Enrollments e RIGHT JOIN Courses c ON e.course_code = c.course_code;

-- Scalar, Correlated, EXISTS
SELECT student_name, (SELECT AVG(marks_obtained) FROM Enrollments) as avg FROM Students LIMIT 1;

SELECT s.student_name FROM Students s WHERE EXISTS (SELECT 1 FROM Enrollments WHERE student_id = s.student_id AND marks_obtained > 90);

-- Set Operation
SELECT student_name FROM Students WHERE department = 'CS'
UNION
SELECT student_name FROM Students WHERE enrollment_year = 2024;

-- Window Function
SELECT student_name, marks_obtained,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY marks_obtained DESC) as rn
FROM Students s JOIN Enrollments e ON s.student_id = e.student_id;
