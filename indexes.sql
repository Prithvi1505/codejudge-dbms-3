CREATE INDEX idx_students_department ON Students(department);
CREATE INDEX idx_enrollments_course ON Enrollments(course_code);
CREATE INDEX idx_enrollments_student_course ON Enrollments(student_id, course_code);
