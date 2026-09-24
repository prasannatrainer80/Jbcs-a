DROP DATABASE IF EXISTS studentdb;

CREATE DATABASE studentdb;

USE studentdb;



CREATE TABLE student
(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    course VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15)
);



CREATE TABLE attendance
(
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,

    student_id INT NOT NULL,

    attendance_date DATE NOT NULL,

    status VARCHAR(10) NOT NULL,

    CONSTRAINT fk_attendance_student
    FOREIGN KEY (student_id)
    REFERENCES student(student_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);




CREATE TABLE marks
(
    marks_id INT PRIMARY KEY AUTO_INCREMENT,

    student_id INT NOT NULL,

    subject VARCHAR(50) NOT NULL,

    marks DECIMAL(5,2) NOT NULL,

    max_marks DECIMAL(5,2) DEFAULT 100,

    CONSTRAINT fk_marks_student
    FOREIGN KEY (student_id)
    REFERENCES student(student_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);




CREATE TABLE fee_payment
(
    payment_id INT PRIMARY KEY AUTO_INCREMENT,

    student_id INT NOT NULL,

    payment_date DATE NOT NULL,

    amount DECIMAL(10,2) NOT NULL,

    payment_mode VARCHAR(20),

    CONSTRAINT fk_fee_student
    FOREIGN KEY (student_id)
    REFERENCES student(student_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);



INSERT INTO student
(student_id, name, gender, course, email, phone)
VALUES

(1, 'Ravi', 'Male', 'Python',
 'ravi@gmail.com', '9876543210'),

(2, 'Priya', 'Female', 'Java',
 'priya@gmail.com', '9876543211'),

(3, 'Kiran', 'Male', 'SQL',
 'kiran@gmail.com', '9876543212'),

(4, 'Anjali', 'Female', 'Python',
 'anjali@gmail.com', '9876543213'),

(5, 'Suresh', 'Male', 'Data Science',
 'suresh@gmail.com', '9876543214'),

(6, 'Lakshmi', 'Female', 'Java',
 'lakshmi@gmail.com', '9876543215'),

(7, 'Arun', 'Male', 'Python',
 'arun@gmail.com', '9876543216'),

(8, 'Sneha', 'Female', 'Data Analytics',
 'sneha@gmail.com', '9876543217');




INSERT INTO attendance
(student_id, attendance_date, status)
VALUES

-- Ravi
(1, '2026-09-01', 'Present'),
(1, '2026-09-02', 'Present'),
(1, '2026-09-03', 'Absent'),
(1, '2026-09-04', 'Present'),
(1, '2026-09-05', 'Present'),

-- Priya
(2, '2026-09-01', 'Present'),
(2, '2026-09-02', 'Present'),
(2, '2026-09-03', 'Present'),
(2, '2026-09-04', 'Present'),
(2, '2026-09-05', 'Absent'),

-- Kiran
(3, '2026-09-01', 'Absent'),
(3, '2026-09-02', 'Present'),
(3, '2026-09-03', 'Present'),
(3, '2026-09-04', 'Present'),
(3, '2026-09-05', 'Present'),

-- Anjali
(4, '2026-09-01', 'Present'),
(4, '2026-09-02', 'Present'),
(4, '2026-09-03', 'Present'),
(4, '2026-09-04', 'Absent'),
(4, '2026-09-05', 'Present'),

-- Suresh
(5, '2026-09-01', 'Present'),
(5, '2026-09-02', 'Absent'),
(5, '2026-09-03', 'Present'),
(5, '2026-09-04', 'Present'),
(5, '2026-09-05', 'Present'),

-- Lakshmi
(6, '2026-09-01', 'Present'),
(6, '2026-09-02', 'Present'),
(6, '2026-09-03', 'Present'),
(6, '2026-09-04', 'Present'),
(6, '2026-09-05', 'Present'),

-- Arun
(7, '2026-09-01', 'Present'),
(7, '2026-09-02', 'Absent'),
(7, '2026-09-03', 'Present'),
(7, '2026-09-04', 'Absent'),
(7, '2026-09-05', 'Present'),

-- Sneha
(8, '2026-09-01', 'Present'),
(8, '2026-09-02', 'Present'),
(8, '2026-09-03', 'Present'),
(8, '2026-09-04', 'Present'),
(8, '2026-09-05', 'Present');




INSERT INTO marks
(student_id, subject, marks, max_marks)
VALUES

-- Ravi
(1, 'Python', 90, 100),
(1, 'SQL', 85, 100),
(1, 'Java', 78, 100),

-- Priya
(2, 'Python', 88, 100),
(2, 'SQL', 92, 100),
(2, 'Java', 95, 100),

-- Kiran
(3, 'Python', 75, 100),
(3, 'SQL', 89, 100),
(3, 'Java', 72, 100),

-- Anjali
(4, 'Python', 94, 100),
(4, 'SQL', 91, 100),
(4, 'Java', 87, 100),

-- Suresh
(5, 'Python', 82, 100),
(5, 'SQL', 86, 100),
(5, 'Data Science', 91, 100),

-- Lakshmi
(6, 'Python', 89, 100),
(6, 'SQL', 93, 100),
(6, 'Java', 90, 100),

-- Arun
(7, 'Python', 76, 100),
(7, 'SQL', 80, 100),
(7, 'Java', 74, 100),

-- Sneha
(8, 'Python', 95, 100),
(8, 'SQL', 94, 100),
(8, 'Data Analytics', 96, 100);



INSERT INTO fee_payment
(student_id, payment_date, amount, payment_mode)
VALUES

-- Ravi
(1, '2026-08-01', 15000, 'Online'),
(1, '2026-09-01', 10000, 'Cash'),

-- Priya
(2, '2026-08-01', 20000, 'Online'),
(2, '2026-09-01', 15000, 'UPI'),

-- Kiran
(3, '2026-08-05', 12000, 'Cash'),
(3, '2026-09-05', 8000, 'Online'),

-- Anjali
(4, '2026-08-03', 18000, 'UPI'),
(4, '2026-09-03', 12000, 'Online'),

-- Suresh
(5, '2026-08-04', 25000, 'Online'),
(5, '2026-09-04', 10000, 'UPI'),

-- Lakshmi
(6, '2026-08-06', 20000, 'Cash'),
(6, '2026-09-06', 15000, 'Online'),

-- Arun
(7, '2026-08-07', 15000, 'UPI'),
(7, '2026-09-07', 5000, 'Cash'),

-- Sneha
(8, '2026-08-08', 22000, 'Online'),
(8, '2026-09-08', 13000, 'UPI');




SELECT * FROM student;

SELECT * FROM attendance;

SELECT * FROM marks;

SELECT * FROM fee_payment;