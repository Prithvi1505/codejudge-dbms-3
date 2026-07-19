PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    enrollment_year INTEGER DEFAULT 2025
);

CREATE TABLE Courses (
    course_code VARCHAR(10) PRIMARY KEY NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    instructor_name VARCHAR(100),
    available_seats INTEGER DEFAULT 50
);

CREATE TABLE Enrollments (
    enrollment_id INTEGER PRIMARY KEY NOT NULL,
    student_id INTEGER NOT NULL,
    course_code VARCHAR(10) NOT NULL,
    marks_obtained DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_code) REFERENCES Courses(course_code)
);
