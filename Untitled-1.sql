CREATE DATABASE employee_task_management;
SHOW DATABASES;
USE employee_task_management;

CREATE TABLE employees(
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects(
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE tasks(
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    task_name VARCHAR(200) NOT NULL,
    description TEXT,
    project_id INT,
    employee_id INT,
    status VARCHAR(30) DEFAULT 'Pending',
    priority VARCHAR(20) DEFAULT 'Medium',
    due_date DATE,

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)

);

INSERT INTO employees
(name, email, department)
VALUES
('Rahul', 'rahul@gmail.com', 'IT');

SELECT * FROM employees;

INSERT INTO projects
(project_name,description,start_date)
VALUES
( 'Employee Management system',
   'Python and MYsql project',
    '2026-10-01'
    );

SELECT * FROM projects;

INSERT INTO tasks
(task_name, description, project_id, employee_id, priority, due_date)
VALUES
( 'Create Login Page',
   'Developer login functionality',
   1,
   1,
   'High',
   '2026-10-05'
   );

SELECT * from tasks;


use employee_task_management;
select * from employees;

select * from projects;