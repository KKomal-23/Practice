create database college;
create database Student;
Create database Employee;
create database Company;
DROP database company;
DROP database Employee;
DROP database student;

USE College;
CREATE TABLE Student( id INT PRIMARY KEY, Name VARCHAR(50), Age INT NOT NULL);
INSERT INTO Student VALUES( 1 , "Stud1" ,21);
INSERT INTO Student VALUES(2 , "Stud2" , 21);
INSERT INTO Student VALUES(3 , "Stud3" , 22);
INSERT INTO Student VALUES(4 , "Stud4" , 20);
INSERT INTO Student VALUES(5 , "Stud5" , 19);

create database college;
create database Student;
Create database Employee;
create database Company;
DROP database company;
DROP database Employee;
DROP database student;

USE College;
CREATE TABLE Student( id INT PRIMARY KEY, Name VARCHAR(50), Age INT NOT NULL);
INSERT INTO Student VALUES( 1 , "Stud1" ,21);
INSERT INTO Student VALUES(2 , "Stud2" , 21);
INSERT INTO Student VALUES(3 , "Stud3" , 22);
INSERT INTO Student VALUES(4 , "Stud4" , 20);
INSERT INTO Student VALUES(5 , "Stud5" , 19);
USE College;
INSERT INTO Student (id, Name, Age) values(6, "stud6", 20) ,(7,"stud7" , 21);
SELECT * from Student;

create database school;
USE school;
create TABLE student(Roll_no INT PRIMARY KEY, Name VARCHAR(50) , Marks FLOAT , Grade VARCHAR(1), City VARCHAR(20)); 
INSERT INTO student(Roll_no , Name, Marks, Grade, City) values
 (101 , "Anil" , 90 , "A" , "Mumbai"),
 (102 , "Prakash" , 85 , "A" , "Pune"),
 (103 , "Ananya" , 56 , "b" , "Delhi"),
 (104 , "Senorita" , 76 , "B" ,"Mumbai"),
 (105 , "Akay" , 96 , "A" , "Pune"),
 (106 , "Sakshi" , 83 ,"A" , "Delhi");
select * from Student;
select Roll_no , Name FROM student;
select distinct City FROM student;
select * FROM student WHERE Marks>80;
select * FROM student WHERE Marks >80 AND City = "Mumbai";
select * FROM student WHERE City IN ("Mumbai","Delhi","Satara");
select * FROM student WHERE City NOT IN ("Mumbai","Delhi","Satara");
select * FROM student LIMIT 3;
select * FROM student WHERE Marks>80 LIMIT 2;
select * FROM student ORDER BY City ASC;
select city, AVG(Marks)
from student
group by city
order by City ASC;
select Grade, count(Name) from student group by Grade;
SET SQL_SAFE_UPDATES = 0;
UPDATE student SET Grade = "o" WHERE Grade = "A";
select Grade FROM student;

DROP TABLE department;
DROP TABLE teacher;
create table department( Id INT PRIMARY KEY, Name VARCHAR(20));
INSERT INTO department(Id , Name) values
(101,"Science"), (102 , "Maths") ,(103,"GK"),(104 ,"English");
DELETE FROM department;

SELECT * FROM department;
UPDATE department
set Id = 105
Where Id = 102;
DROP TABLE teacher;
create table teacher(Id INT PRIMARY KEY , 
Name VARCHAR(20), 
Dept_id INT,
FOREIGN KEY (Dept_id) REFERENCES department(Id)
ON UPDATE CASCADE
ON DELETE CASCADE);
INSERT INTO teacher( Id,Name, Dept_id) values 
(1 , "Adam", 101), (2 , "KP", 102), (3 ,"Aasha" , 103),(4,"Pooja" ,104),
(5,"Kalyani",103),(6,"Deepak",102),(7,"mandar" ,101);
select * FROM teacher;







