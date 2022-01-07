-- create database 
CREATE DATABASE employee;


-- create table and drop tables
USE employee;

CREATE TABLE empDetails (
    id int not null auto_increment primary key,
    empName varchar(45) not null,
    phoneNum varchar(15),
    email varchar(30),
    age int
);

DROP TABLE empDetails;


-- insert, delete, and update records
INSERT INTO empDetails (name, empName, phoneNum, email, age) VALUE('John Doe', '1234567', 'doe@turntabl.io', 25);
INSERT INTO empDetails (name, empName, phoneNum, email, age) VALUE('Frank Siri', '7654321', 'siri@turntabl.io', 29);
INSERT INTO empDetails (name, empName, phoneNum, email, age) VALUE('Franklina Akka', '1246810', 'akka@turntabl.io', 23);

UPDATE empDetails SET email="admin@turntabl.io" WHERE empName="Franklina Akka";

DELETE FROM empDetails WHERE email="doe@turntabl.io";


-- simple select query 
SELECT * FROM empDetails;



