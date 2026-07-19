-- Insert into Students
INSERT INTO Students (student_id, student_name, department, enrollment_year) VALUES
(1, 'Alice', 'CS', 2024), (2, 'Bob', 'CS', 2024), (3, 'Charlie', 'Math', 2023);

-- Insert into Courses
INSERT INTO Courses (course_code, course_name, instructor_name, available_seats) VALUES
('CS101', 'Intro to CS', 'Dr. Smith', 40),
('CS202', 'Data Structures', 'Dr. Lee', 30);

-- Enrollments
INSERT INTO Enrollments (enrollment_id, student_id, course_code, marks_obtained) VALUES
(1, 1, 'CS101', 85), (2, 2, 'CS101', 92);
