DROP DATABASE IF EXISTS empdatabase;


CREATE DATABASE empdatabase;

USE empdatabase;


CREATE TABLE employee(
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name TINYTEXT,
    last_name TINYTEXT,
    salary FLOAT(10,2),
    employee_type ENUM('Manager','Administrator','Operational')
);

INSERT INTO employee (first_name,last_name,salary,employee_type)
VALUES ('Melanie','Smith',90000, 'Manager'), ('Walid','Khalil',120000, 'Administrator'),
('Sanmeet','Kaur', 60000, 'Operational');


SELECT * FROM employee;

-- changing delimeter
DELIMITER //

CREATE FUNCTION empdatabase.generate_email(first_name TINYTEXT,last_name TINYTEXT)
    RETURNS TINYTEXT
    BEGIN
        DECLARE email TINYTEXT;
        SELECT LOWER(CONCAT(SUBSTRING(first_name,1,1),last_name,"@staff.organization.com")) INTO email;
        RETURN email;
    END//

DELIMITER ;


show create function generate_email; -- see how function is defined